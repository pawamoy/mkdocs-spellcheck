"""This module contains the different spell checking backends."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from mkdocs.structure.pages import Page


class Backend(ABC):
    """Abstract class for spelling backends."""

    @abstractmethod
    def __init__(self, config: dict[str, Any], known_words: set[str] | None = None) -> None:
        """Initialize the backend.

        Parameters:
            config: User configuration from `mkdocs.yml`.
            known_words: Globally known words.
        """
        raise NotImplementedError

    @abstractmethod
    def check(self, page: Page, word: str) -> None:
        """Check a word appearing in a page.

        Parameters:
            page: The MkDocs page the word appears in.
            word: The word to check.
        """
        raise NotImplementedError
