# Coding Conventions

When writing Python code for this project, please

* Use `import module` and not `from module import name`
* you may `from . import module` if the imporing module is in the same namespace
* avoid namesapce inflation, e.g. use `parsers.text.Text()` and not `parsers.text_parser.TextParser()`
* avoid shorthand, e.g. use `connection`, `packet`, `error`, `instance`, `filename` instead of `conn`, `pkt`, `err`, `inst`, `fname`. Exceptions to this rule are things like `xml`.
* when writing code, don't be shy about introducing namespaces.
