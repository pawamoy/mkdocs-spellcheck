# Backend for the `symspellpy` library.

from __future__ import annotations

from importlib import resources
from typing import TYPE_CHECKING, Any

from mkdocs.plugins import get_plugin_logger

from mkdocs_spellcheck._internal.backends import Backend

if TYPE_CHECKING:
    from mkdocs.structure.pages import Page


_logger = get_plugin_logger(__name__)


try:
    from symspellpy import SymSpell, Verbosity
except ImportError:

    class SymspellpyBackend(Backend):
        """Backend for the `symspellpy` library."""

        def __init__(self, config: dict[str, Any], known_words: set[str] | None = None) -> None:  # noqa: ARG002
            """Initialize the `symspellpy` backend.

            This backend is a stub because `symspellpy` is not installed.
            It will not perform any spell checking.

            Parameters:
                config: User configuration from `mkdocs.yml`.
                known_words: Globally known words.
            """
            _logger.warning("The `symspellpy` backend is not available. Please install the `symspellpy` package.")

        def check(self, page: Page, word: str) -> None:
            pass
else:

    class SymspellpyBackend(Backend):  # type: ignore[no-redef]
        """Backend for the `symspellpy` library."""

        def __init__(self, config: dict[str, Any], known_words: set[str] | None = None) -> None:  # noqa: ARG002
            """Initialize the `symspellpy` backend.

            This backend needs to load dictionaries provided
            by `symspellpy` itself.

            Parameters:
                config: User configuration from `mkdocs.yml`.
                known_words: Globally known words.
            """
            self.spell = SymSpell()
            """The `symspellpy` spell checker."""
            dictionary_res = resources.files("symspellpy").joinpath("frequency_dictionary_en_82_765.txt")
            with resources.as_file(dictionary_res) as dictionary_path:
                self.spell.load_dictionary(dictionary_path, 0, 1)

        def check(self, page: Page, word: str) -> None:
            """Check a word against the `symspellpy` dictionary."""
            suggestions = self.spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)
            if suggestions:
                candidates = "', '".join(suggestion.term for suggestion in suggestions if suggestion.term != word)
                if candidates:
                    _logger.warning(
                        f"(symspellpy) {page.file.src_path}: Misspelled '{word}', did you mean '{candidates}'?",
                    )
            else:
                _logger.warning(f"(symspellpy) {page.file.src_path}: Misspelled '{word}', no suggestions")
