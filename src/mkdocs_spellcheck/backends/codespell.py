"""Deprecated. Import directly from `mkdocs_spellcheck` instead."""

# YORE: Bump 2: Remove file.

import warnings
from typing import Any

from mkdocs_spellcheck._internal.backends import codespell


def __getattr__(name: str) -> Any:
    warnings.warn(
        "Importing from 'mkdocs_spellcheck.backends.codespell' is deprecated. Import directly from 'mkdocs_spellcheck' instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return getattr(codespell, name)
