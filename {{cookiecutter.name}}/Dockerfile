FROM python:3.13-slim-trixie AS base
ARG COMMIT_HASH=unknown

COPY --from=ghcr.io/astral-sh/uv:0.13 /uv /uvx /bin/

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never

WORKDIR /opt/{{cookiecutter.name}}

# install dependencies first, so this layer is cached until the lockfile changes
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev --no-install-project

COPY README.md ./
COPY src src
RUN uv sync --locked --no-dev

ENV PATH="/opt/{{cookiecutter.name}}/.venv/bin:${PATH}"

RUN echo $COMMIT_HASH > /commit_hash
