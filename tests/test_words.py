"""Tests for the `cli` module."""

import pytest

from mkdocs_spellcheck.words import get_words


@pytest.mark.parametrize("tag", ["p", "em", "div", "article"])
def test_remove_tags(tag: str):
    """Assert tags are removed from HTML text.

    Parameters:
        tag: Some HTML tag (parametrized).
    """
    html = f"<{tag}>Some text.</{tag}><br><hr/>"
    words = get_words(html, min_length=1)
    assert tag not in words


def test_remove_single_tags():
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
def test_ignore_known_words(text, known_words, expected):
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
def test_ignore_too_short_words(text, min_length, expected):
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
def test_ignore_text_in_code_tags(text, ignore_code, expected):
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
def test_allow_unicode_characters(text, allow_unicode, expected):
    """Assert known words are correctly removed.

    Parameters:
        text: Some text (parametrized).
        allow_unicode: Whether to allow unicode characters in words (parametrized).
        expected: Expected list result (parametrized).
    """
    assert get_words(text, allow_unicode=allow_unicode) == expected
