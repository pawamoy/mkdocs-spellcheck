# This module contains a function to retrieve words from HTML text.

from __future__ import annotations

import re
import unicodedata
from functools import partial
from html.parser import HTMLParser
from io import StringIO

_spell_check_guard_on = "mkdocs-spellcheck-on"
_spell_check_guard_off = "mkdocs-spellcheck-off"


class _MLStripper(HTMLParser):
    def __init__(self, ignore_code: bool = True) -> None:  # noqa: FBT001,FBT002
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()
        self.ignore_code = ignore_code
        self.in_code_tag = False
        self.in_guard = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:  # noqa: ARG002
        if tag == "code":
            self.in_code_tag = True
        self.text.write(" ")

    def handle_endtag(self, tag: str) -> None:
        if tag == "code":
            self.in_code_tag = False

    def handle_comment(self, data: str) -> None:
        data = data.strip()

        if not self.in_code_tag:
            if data == _spell_check_guard_off:
                self.in_guard = True
            elif data == _spell_check_guard_on:
                self.in_guard = False

    def handle_data(self, data: str) -> None:
        if self.ignore_code and self.in_code_tag:
            return

        if self.in_guard:
            return

        self.text.write(data)

    def get_data(self) -> str:
        return self.text.getvalue()


def _strip(html: str, ignore_code: bool) -> str:  # noqa: FBT001
    stripper = _MLStripper(ignore_code)
    stripper.feed(html)
    return stripper.get_data()


_not_letters_nor_spaces = re.compile(r"(?:(\B\'|\'\B|\B\'\B|\'s)|[^\w\s\'-])")
_dashes_or_spaces = re.compile(r"[-_\s]+")


def _normalize(value: str, allow_unicode: bool = False) -> str:  # noqa: FBT001,FBT002
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = _not_letters_nor_spaces.sub(" ", value)
    return _dashes_or_spaces.sub("-", value).strip("-_")


def _keep_word(word: str, min_length: int, max_capital: int) -> bool:
    if len(word) < min_length:
        return False
    capitals = 0
    for char in word:
        if char.isdigit():
            return False
        if char.isupper():
            capitals += 1
            if capitals > max_capital:
                return False
    return True


def get_words(
    html: str,
    *,
    known_words: set[str] | None = None,
    min_length: int = 2,
    max_capital: int = 1,
    ignore_code: bool = True,
    allow_unicode: bool = True,
) -> list[str]:
    """Get words in HTML text.

    Parameters:
        html: The HTML text.
        known_words: Words to exclude.
        min_length: Words minimum length.
        max_capital: Maximum number of capital letters.
        ignore_code: Ignore words in code tags.
        allow_unicode: Keep unicode characters.

    Returns:
        A list of words.
    """
    known_words = known_words or set()
    keep = partial(_keep_word, min_length=min_length, max_capital=max_capital)
    filtered = filter(keep, _normalize(_strip(html, ignore_code), allow_unicode).split("-"))
    words = {word.lower() for word in filtered}
    return sorted(words - known_words)
