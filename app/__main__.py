"""Entry point: `python -m app [name]`."""

import sys

from app.greeter import greet


def main() -> int:
    """Print a greeting and exit 0."""
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
