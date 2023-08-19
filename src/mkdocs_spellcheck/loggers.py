"""Logging functions."""

from __future__ import annotations

import logging
from typing import Any, MutableMapping


# TODO: remove once support for MkDocs <1.5 is dropped (use built-in)
class PrefixedLogger(logging.LoggerAdapter):  # noqa: D101
    def __init__(self, prefix: str, logger: logging.Logger) -> None:  # noqa: D107
        super().__init__(logger, {})
        self.prefix = prefix

    def process(self, msg: str, kwargs: MutableMapping[str, Any]) -> tuple[str, Any]:  # noqa: D102
        return f"{self.prefix}: {msg}", kwargs


def get_plugin_logger(name: str) -> PrefixedLogger:  # noqa: D103
    logger = logging.getLogger(f"mkdocs.plugins.{name}")
    return PrefixedLogger(name.split(".", 1)[0], logger)
