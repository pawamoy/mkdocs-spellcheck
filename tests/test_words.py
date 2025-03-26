"""Tests for the `cli` module."""

from __future__ import annotations

import pytest

from mkdocs_spellcheck import get_words


@pytest.mark.parametrize("tag", ["p", "em", "div", "article"])
def test_remove_tags(tag: str) -> None:
    """Assert tags are removed from HTML text.

    Parameters:
        tag: Some HTML tag (parametrized).
    """
    html = f"<{tag}>Some text.</{tag}><br><hr/>"
    words = get_words(html, min_length=1)
    assert tag not in words


def test_remove_single_tags() -> None:
    """Assert single tags like `br` are removed from HTML text."""
    html = "Some text.<br><br/><br /><img /></br>"
    words = get_words(html, min_length=1)
    assert "br" not in words
    assert "img" not in words


@pytest.mark.parametrize(
    ("text", "known_words", "expected"),
    [
        ("hello", {}, ["hello"]),
        ("hello", {"hello"}, []),
        ("hello", {"world"}, ["hello"]),
    ],
)
def test_ignore_known_words(text: str, known_words: set[str], expected: list[str]) -> None:
    """Assert known words are correctly removed.

    Parameters:
        text: Some text (parametrized).
        known_words: Some known words (parametrized).
        expected: Expected list result (parametrized).
    """
    assert get_words(text, known_words=known_words) == expected


@pytest.mark.parametrize(
    ("text", "min_length", "expected"),
    [
        ("a bb ccc", 0, ["a", "bb", "ccc"]),
        ("a bb ccc", 1, ["a", "bb", "ccc"]),
        ("a bb ccc", 2, ["bb", "ccc"]),
        ("a bb ccc", 3, ["ccc"]),
        ("a bb ccc", 4, []),
    ],
)
def test_ignore_too_short_words(text: str, min_length: int, expected: list[str]) -> None:
    """Assert known words are correctly removed.

    Parameters:
        text: Some text (parametrized).
        min_length: Minimum word length (parametrized).
        expected: Expected list result (parametrized).
    """
    assert get_words(text, min_length=min_length) == expected


@pytest.mark.parametrize(
    ("text", "ignore_code", "expected"),
    [
        ("Hello <code>world!<code>", True, ["hello"]),
        ("Hello <code>world!<code>", False, ["hello", "world"]),
    ],
)
def test_ignore_text_in_code_tags(text: str, ignore_code: bool, expected: list[str]) -> None:
    """Assert known words are correctly removed.

    Parameters:
        text: Some text (parametrized).
        ignore_code: Whether to ignore words in code tags (parametrized).
        expected: Expected list result (parametrized).
    """
    assert get_words(text, ignore_code=ignore_code) == expected


@pytest.mark.parametrize(
    ("text", "allow_unicode", "expected"),
    [
        ("Hello world! ハローワールド!", True, ["hello", "world", "ハローワールド"]),
        ("Hello world! ハローワールド!", False, ["hello", "world"]),
    ],
)
def test_allow_unicode_characters(text: str, allow_unicode: bool, expected: list[str]) -> None:
    """Assert known words are correctly removed.

    Parameters:
        text: Some text (parametrized).
        allow_unicode: Whether to allow unicode characters in words (parametrized).
        expected: Expected list result (parametrized).
    """
    assert get_words(text, allow_unicode=allow_unicode) == expected


def test_prevent_words_concatenation() -> None:
    """Assert words are not concatenated when removing HTML tags."""
    html = "<p>Hello</p><p>world!</p>"
    assert get_words(html) == ["hello", "world"]


def test_reset_after_code_endtag() -> None:
    """Assert the HTML stripper correctly resets its state after finding a `</code>` end tag."""
    html = "<p>Some</p><code>code</code><p>snippet</p>"
    assert "snippet" in get_words(html, ignore_code=True)
