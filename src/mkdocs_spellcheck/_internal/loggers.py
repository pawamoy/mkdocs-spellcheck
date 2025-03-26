"""Logging functions."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import MutableMapping


# TODO: remove once support for MkDocs <1.5 is dropped (use built-in)
class PrefixedLogger(logging.LoggerAdapter):
    def __init__(self, prefix: str, logger: logging.Logger) -> None:
        super().__init__(logger, {})
        self.prefix = prefix

    def process(self, msg: str, kwargs: MutableMapping[str, Any]) -> tuple[str, Any]:
        return f"{self.prefix}: {msg}", kwargs


def get_plugin_logger(name: str) -> PrefixedLogger:
    logger = logging.getLogger(f"mkdocs.plugins.{name}")
    return PrefixedLogger(name.split(".", 1)[0], logger)
