FROM python:3.12

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

COPY --from=ghcr.io/astral-sh/uv:0.5.22 /uv /bin/uv

WORKDIR /app

ENV ALL_PROXY=socks5h://host.docker.internal:1080 \
    HTTP_PROXY=${ALL_PROXY} \
    HTTPS_PROXY=${ALL_PROXY}

ENV PYTHONPATH=/app

RUN apt update && \
    apt install -y libgl1 libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY ../pyproject.toml ../uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
  uv sync --frozen --no-install-project --no-dev

COPY ./app ./app

RUN chmod +x app/entrypoint.sh

ENTRYPOINT ["/app/app/entrypoint.sh"]