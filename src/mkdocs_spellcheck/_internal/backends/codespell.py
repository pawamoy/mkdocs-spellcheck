# Backend for the `codespell` tool.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any

from mkdocs.plugins import get_plugin_logger

from mkdocs_spellcheck._internal.backends import Backend

if TYPE_CHECKING:
    from mkdocs.structure.pages import Page

_logger = get_plugin_logger(__name__)


try:
    from codespell_lib._codespell import (
        Misspelling,
        _builtin_default,
        _builtin_dictionaries,
        _data_root,
        build_dict,
        fix_case,
    )
except ImportError:

    class CodespellBackend(Backend):
        """Backend for the `codespell` tool."""

        def __init__(self, config: dict[str, Any], known_words: set[str] | None = None) -> None:  # noqa: ARG002
            """Initialize the `codespell` backend.

            This backend is a stub because `codespell` is not installed.
            It will not perform any spell checking.

            Parameters:
                config: User configuration from `mkdocs.yml`.
                known_words: Globally known words.
            """
            _logger.warning("The `codespell` backend is not available. Please install the `codespell` package.")

        def check(self, page: Page, word: str) -> None:
            pass
else:
    _DEFAULT_DICTS = _builtin_default.split(",")

    class CodespellBackend(Backend):  # type: ignore[no-redef]
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
            for dictionary in config.get("dictionaries", _DEFAULT_DICTS):
                for builtin in _builtin_dictionaries:
                    if builtin[0] == dictionary:
                        use_dictionaries.append(os.path.join(_data_root, f"dictionary{builtin[2]}.txt"))

            self.misspellings: dict[str, Misspelling] = {}
            """A mapping of misspelled words to their corrections."""

            for dictionary in use_dictionaries:
                build_dict(dictionary, self.misspellings, known_words)

        def check(self, page: Page, word: str) -> None:
            """Check a word against the `codespell` misspellings."""
            if word in self.misspellings:
                # reason = self.misspellings[word].reason
                fixword = fix_case(word, self.misspellings[word].data)
                _logger.warning(f"(codespell) {page.file.src_path}: Misspelled '{word}', did you mean '{fixword}'?")
