# README

do NOT update the README unless I explicitly ask you to.

# Coding Conventions

When writing Python code for this project, please

* Use `import module` and not `from module import name`
* you may `from . import module` if the imporing module is in the same namespace
* avoid namesapce inflation, e.g. use `parsers.text.Text()` and not `parsers.text_parser.TextParser()`

# Claude Context Window 

Your context window will be automatically compacted as it approaches its limit,
allowing you to continue working indefinitely from where you left off.
Therefore, do not stop tasks early due to token budget concerns. As you
approach your token budget limit, save your current progress and state to
memory before the context window refreshes. Always be as persistent and
autonomous as possible and complete tasks fully, even if the end of your budget
is approaching. Never artificially stop any task early regardless of the
context remaining.
