"""Backend for the `codespell` tool."""

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any

from codespell_lib._codespell import (
    Misspelling,
    _builtin_default,
    _builtin_dictionaries,
    _data_root,
    build_dict,
    fix_case,
)

from mkdocs_spellcheck.backends import Backend
from mkdocs_spellcheck.loggers import get_plugin_logger

if TYPE_CHECKING:
    from mkdocs.structure.pages import Page

logger = get_plugin_logger(__name__)

DEFAULT_DICTS = _builtin_default.split(",")


class CodespellBackend(Backend):
    """Backend for the `codespell` tool."""

    def __init__(self, config: dict[str, Any], known_words: set[str] | None = None) -> None:
        """Initialize the `codespell` backend.

        This backend needs to build a list of misspellings based
        on dictionaries provided by `codespell` itself.

        Parameters:
            config: User configuration from `mkdocs.yml`.
            known_words: Globally known words.
        """
        known_words = known_words or set()
        use_dictionaries = []
        for dictionary in config.get("dictionaries", DEFAULT_DICTS):
            for builtin in _builtin_dictionaries:
                if builtin[0] == dictionary:
                    use_dictionaries.append(os.path.join(_data_root, f"dictionary{builtin[2]}.txt"))
        self.misspellings: dict[str, Misspelling] = {}
        for dictionary in use_dictionaries:
            build_dict(dictionary, self.misspellings, known_words)

    def check(self, page: Page, word: str) -> None:  # noqa: D102
        if word in self.misspellings:
            # reason = self.misspellings[word].reason
            fixword = fix_case(word, self.misspellings[word].data)
            logger.warning(f"(codespell) {page.file.src_path}: Misspelled '{word}', did you mean '{fixword}'?")
