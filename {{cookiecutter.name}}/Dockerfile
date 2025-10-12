FROM python:3.13-trixie AS base
ARG COMMIT_HASH=unknown

RUN apt-get update -y
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

WORKDIR /opt/{{cookiecutter.name}}

RUN touch README.md
COPY src src
COPY pyproject.toml .
COPY uv.lock .

ENV PATH="/root/.local/bin:${PATH}"
RUN uv sync

RUN echo $COMMIT_HASH > /commit_hash
