"""The app's only real logic."""

import os


def app_version() -> str:
    """Return the version baked into the image at build time ("dev" when run locally)."""
    return os.environ.get("APP_VERSION", "dev")


def greet(name: str) -> str:
    """Build the greeting the container prints on start - test."""
    clean = name.strip() or "world"
    return f"Hello, {clean}! testme {app_version()} is alive."
