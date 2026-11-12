"""Tests for the PR title validator."""

import pytest

from tools.pr_title import is_valid_title, main


@pytest.mark.parametrize(
    "title",
    ["TEST-1: first", "TEST-42 add greeting", "TEST-1234", "TEST-7:no space"],
)
def test_accepts_prefixed_titles(title):
    assert is_valid_title(title)


@pytest.mark.parametrize(
    "title",
    ["", "add greeting", "test-1: lowercase", "TEST-: no number", "TEST-12abc", "fix TEST-12"],
)
def test_rejects_unprefixed_titles(title):
    assert not is_valid_title(title)


def test_main_exit_codes():
    assert main(["pr_title", "TEST-3: ok"]) == 0
    assert main(["pr_title", "nope"]) == 1
    assert main(["pr_title"]) == 2
