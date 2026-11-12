FROM python:3.13-slim

# CI passes the git commit SHA here so the running container can report which build it is.
ARG APP_VERSION=dev
ENV APP_VERSION=${APP_VERSION} \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
LABEL org.opencontainers.image.title="testme" \
      org.opencontainers.image.revision="${APP_VERSION}"

WORKDIR /app
COPY app/ ./app/

# Don't run as root inside the container.
RUN useradd --create-home --uid 10001 appuser
USER appuser

ENTRYPOINT ["python", "-m", "app"]
