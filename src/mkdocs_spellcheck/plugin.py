"""Deprecated. Import directly from `mkdocs_spellcheck` instead."""

# YORE: Bump 2: Remove file.

import warnings
from typing import Any

from mkdocs_spellcheck._internal import plugin


def __getattr__(name: str) -> Any:
    warnings.warn(
        "Importing from 'mkdocs_spellcheck.plugin' is deprecated. Import directly from 'mkdocs_spellcheck' instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return getattr(plugin, name)
