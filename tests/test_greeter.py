"""Tests for the greeting logic."""

from app.greeter import greet


def test_greets_by_name(monkeypatch):
    monkeypatch.setenv("APP_VERSION", "abc1234")
    assert greet("Guy") == "Hello, Guy! testme abc1234 is alive."


def test_blank_name_falls_back_to_world(monkeypatch):
    monkeypatch.delenv("APP_VERSION", raising=False)
    assert greet("   ") == "Hello, world! testme dev is alive."
