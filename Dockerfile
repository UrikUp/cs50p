# =========================
# Builder stage
# =========================
FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim AS builder

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_NO_DEV=1 \
    UV_PYTHON_DOWNLOADS=0 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copy ONLY dependency files first
# This maximizes Docker layer caching
COPY pyproject.toml uv.lock ./

# Install dependencies separately
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-install-project

# Copy application source later
COPY . .

# Install project itself
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked


# =========================
# Runtime stage
# =========================
FROM python:3.14-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

# Create non-root user
RUN groupadd --system --gid 999 nonroot \
 && useradd --system --gid 999 --uid 999 \
    --create-home nonroot

WORKDIR /app

# Copy built app from builder
COPY --from=builder --chown=nonroot:nonroot /app /app

# Make entrypoint executable
RUN chmod +x /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh \
    && chown -R nonroot:nonroot /app

USER nonroot

ENTRYPOINT ["/app/entrypoint.sh"]

# Example FastAPI command
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
