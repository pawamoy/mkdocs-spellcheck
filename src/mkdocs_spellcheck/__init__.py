"""MkDocs SpellCheck package.

A spell checker plugin for MkDocs.
"""

from __future__ import annotations

from mkdocs_spellcheck._internal.backends import Backend
from mkdocs_spellcheck._internal.backends.codespell import CodespellBackend
from mkdocs_spellcheck._internal.backends.symspellpy import SymspellpyBackend
from mkdocs_spellcheck._internal.plugin import SpellCheckPlugin, load_backend
from mkdocs_spellcheck._internal.words import get_words

__all__: list[str] = [
    "Backend",
    "CodespellBackend",
    "SpellCheckPlugin",
    "SymspellpyBackend",
    "get_words",
    "load_backend",
]
