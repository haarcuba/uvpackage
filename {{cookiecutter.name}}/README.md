# {{cookiecutter.name}} - {{cookiecutter.description}}

## Root Convention

All commands are [assumed to run from the root of the project] - the directory in which _this README_ is located.

## Installation

This project uses [uv](https://docs.astral.sh/uv/getting-started/installation/). Install uv however you like. Then run:

    $ uv sync

This will setup a Python virtual environment and install `toynotes` as a package in editable mode, with all its dependencies.

## Aliases

Load useful aliases

    $ source aliases.sh

## CLI Entrypoint

You can run the main CLI entry point with:

    $ {{cookiecutter.name}}-cli --help

Or, if you are outside the virtual environment, you can run:

    $ poetry run {{cookiecutter.name}}-cli --help

## Installation from a Wheel file

If you have a wheel distribution of this software, you can install it with `pip`

    $ pip install /path/to/{{cookiecutter.name}}-wheel-file.whl

It will then be available to import as `import {{cookiecutter.name}}` and to run as a command using `{{cookiecutter.name}}-cli`.
