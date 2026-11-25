#!/usr/bin/env python3
"""SessionEnd hook: give the session a sensible name and log it to <project root>/sessions.md.

Naming priority:
  1. a title you set yourself with /rename (kept as-is)
  2. the git branch, unless it is main/master/detached
  3. Claude Code's auto-generated content title (ai-title)
  4. the first user prompt, truncated
"""
import datetime
import json
import os
import re
import subprocess
import sys

DEFAULT_BRANCHES = {"main", "master", "HEAD", ""}


def read_transcript(path):
    entries = []
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                try:
                    entries.append(json.loads(line))
                except ValueError:
                    pass
    except OSError:
        pass
    return entries


def git_branch(cwd):
    try:
        out = subprocess.run(
            ["git", "-C", cwd, "branch", "--show-current"],
            capture_output=True, text=True, timeout=5,
        )
        return out.stdout.strip() if out.returncode == 0 else ""
    except Exception:
        return ""


def first_user_prompt(entries):
    for e in entries:
        if e.get("type") != "user" or e.get("isMeta") or e.get("isSidechain"):
            continue
        content = (e.get("message") or {}).get("content")
        if isinstance(content, list):
            content = " ".join(
                c.get("text", "") for c in content
                if isinstance(c, dict) and c.get("type") == "text"
            )
        if not isinstance(content, str):
            continue
        text = re.sub(r"<[^>]+>.*?</[^>]+>", " ", content, flags=re.S)  # drop injected tags
        text = " ".join(text.split())
        if text and not text.startswith("/"):
            return text[:60].rstrip() + ("…" if len(text) > 60 else "")
    return ""


def last_value(entries, typ, key):
    vals = [e.get(key) for e in entries if e.get("type") == typ and e.get(key)]
    return vals[-1] if vals else ""


def main():
    data = json.load(sys.stdin)
    session_id = data.get("session_id", "")
    transcript = data.get("transcript_path", "")
    cwd = data.get("cwd") or os.getcwd()

    entries = read_transcript(transcript)
    if not any(e.get("type") == "user" for e in entries):
        return  # empty session, nothing worth logging

    name = last_value(entries, "custom-title", "customTitle")
    already_named = bool(name)
    if not name:
        branch = git_branch(cwd)
        if branch not in DEFAULT_BRANCHES:
            name = branch
    if not name:
        name = last_value(entries, "ai-title", "aiTitle")
    if not name:
        name = first_user_prompt(entries)
    if not name:
        return

    # Rename the session (same record /rename writes).
    if not already_named and transcript:
        with open(transcript, "a", encoding="utf-8") as f:
            f.write(json.dumps({"type": "custom-title", "customTitle": name,
                                "sessionId": session_id}) + "\n")

    # Log to <project root>/sessions.md, once per session id (resumed sessions are not duplicated).
    log = os.path.join(os.environ.get("CLAUDE_PROJECT_DIR") or cwd, "sessions.md")
    try:
        with open(log, encoding="utf-8") as f:
            if session_id and session_id in f.read():
                return
    except FileNotFoundError:
        pass
    today = datetime.date.today().isoformat()
    with open(log, "a", encoding="utf-8") as f:
        f.write(f"- {today} — **{name}** — `claude -r {session_id}`\n")


if __name__ == "__main__":
    main()
