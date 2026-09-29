# SPDX-License-Identifier: ISC
#
# ISC License
#
# Copyright (c) 2022, Timothée Mazzucotelli and contributors
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

# This module contains the different spell checking backends.

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
