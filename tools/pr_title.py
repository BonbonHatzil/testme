"""Fail the pipeline unless the PR title starts with a TEST-<number> ticket prefix.

Usage: python -m tools.pr_title "TEST-12: add greeting"
"""

import re
import sys

# TEST-<digits>, then a colon, a space, or the end of the title.
# Accepts "TEST-12: fix", "TEST-12 fix", "TEST-12". Rejects "test-12", "TEST-12abc", "fix TEST-12".
TITLE_PATTERN = re.compile(r"^TEST-\d+(?::|\s|$)")


def is_valid_title(title: str) -> bool:
    """Return True when the title carries the TEST-<number> prefix."""
    return bool(TITLE_PATTERN.match(title))


def main(argv: list[str]) -> int:
    """Validate argv[1] and return a process exit code."""
    if len(argv) != 2:
        print('usage: python -m tools.pr_title "<PR title>"', file=sys.stderr)
        return 2

    title = argv[1]
    if is_valid_title(title):
        print(f"OK: PR title has a TEST-<number> prefix: {title!r}")
        return 0

    # ::error:: is a GitHub Actions workflow command: it shows up as a red annotation on the run.
    print(
        f"::error title=Bad PR title::{title!r} must start with TEST-<number>, "
        "e.g. 'TEST-42: add greeting'"
    )
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
