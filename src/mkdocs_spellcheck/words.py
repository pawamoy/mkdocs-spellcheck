"""This module contains a function to retrieve words from HTML text."""

from __future__ import annotations

import re
import unicodedata
from functools import partial
from html.parser import HTMLParser
from io import StringIO


class _MLStripper(HTMLParser):
    def __init__(self, ignore_code=True):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()
        self.ignore_code = ignore_code
        self.in_code_tag = False

    def handle_starttag(self, tag, attrs):
        if tag == "code":
            self.in_code_tag = True

    def handle_stoptag(self, tag, attrs):
        if tag == "code":
            self.in_code_tag = False

    def handle_data(self, data):
        if not (self.ignore_code and self.in_code_tag):
            self.text.write(data)

    def get_data(self):
        return self.text.getvalue()


def _strip_tags(html, ignore_code):
    stripper = _MLStripper(ignore_code)
    stripper.feed(html)
    return stripper.get_data()


not_letters_nor_spaces = re.compile(r"[^\w\s-]")
dashes_or_spaces = re.compile(r"[-\s]+")


def _slugify(value, allow_unicode=False):
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = not_letters_nor_spaces.sub(" ", value.lower())
    return dashes_or_spaces.sub("-", value).strip("-_")


def _keep_word(word, min_length):
    if len(word) < min_length:
        return False
    for char in word:
        if char.isdigit():
            return False
    return True


def get_words(
    html: str,
    known_words: set[str] | None = None,
    min_length: int = 2,
    ignore_code: bool = True,
    allow_unicode: bool = True,
) -> list[str]:
    """Get words in HTML text.

    Parameters:
        html: The HTML text.
        known_words: Words to exclude.
        min_length: Words minimum length.
        ignore_code: Ignore words in code tags.
        allow_unicode: Keep unicode characters.

    Returns:
        A list of words.
    """
    known_words = known_words or set()
    keep = partial(_keep_word, min_length=min_length)
    words = filter(keep, _slugify(_strip_tags(html, ignore_code), allow_unicode).split("-"))
    return sorted(set(words) - known_words)
