"""MkDocs SpellCheck package.

A spell checker plugin for MkDocs.
"""

from __future__ import annotations

from fnmatch import fnmatch
from pathlib import Path
from typing import TYPE_CHECKING, Any

from mkdocs.config.config_options import Type as MkType
from mkdocs.plugins import BasePlugin

from mkdocs_spellcheck.loggers import get_plugin_logger
from mkdocs_spellcheck.words import get_words

if TYPE_CHECKING:
    from mkdocs.config.defaults import MkDocsConfig
    from mkdocs.structure.pages import Page

    from mkdocs_spellcheck.backends import Backend

logger = get_plugin_logger(__name__)


def load_backend(name: str) -> type[Backend]:
    """Load the specified backend.

    This function imports the specified backend and returns its class.
    It is important not to import the backends at the top level, as
    they may not be installed.

    Arguments:
        name: The name of the backend to load.

    Returns:
        The backend class.
    """
    if name == "symspellpy":
        from mkdocs_spellcheck.backends import symspellpy

        return symspellpy.SymspellpyBackend

    if name == "codespell":
        from mkdocs_spellcheck.backends import codespell

        return codespell.CodespellBackend

    raise ValueError(f"Unknown backend: {name}")


class SpellCheckPlugin(BasePlugin):
    """A `mkdocs` plugin.

    This plugin defines the following event hooks:

    - `on_config`
    - `on_page_content`

    Check the [Developing Plugins](https://www.mkdocs.org/user-guide/plugins/#developing-plugins) page of `mkdocs`
    for more information about its plugin system.
    """

    config_scheme: tuple[tuple[str, MkType], ...] = (
        ("strict_only", MkType(bool, default=False)),
        ("backends", MkType(list, default=["symspellpy"])),
        ("known_words", MkType((str, list), default=[])),
        ("skip_files", MkType(list, default=[])),
        ("min_length", MkType(int, default=2)),
        ("max_capital", MkType(int, default=1)),
        ("ignore_code", MkType(bool, default=True)),
        ("allow_unicode", MkType(bool, default=False)),
    )

    def __init__(self) -> None:  # noqa: D107
        self.known_words: set[str] = set()
        super().__init__()

    def on_config(self, config: MkDocsConfig) -> MkDocsConfig | None:
        """Load words to ignore.

        Hook for the [`on_config` event](https://www.mkdocs.org/user-guide/plugins/#on_config).

        Arguments:
            config: The MkDocs config object.

        Returns:
            The modified config.
        """
        self.strict_only = self.config["strict_only"]
        self.backends_config = self.config["backends"]
        self.skip_files = self.config["skip_files"]
        self.min_length = self.config["min_length"]
        self.max_capital = self.config["max_capital"]
        self.ignore_code = self.config["ignore_code"]
        self.allow_unicode = self.config["allow_unicode"]
        self.run = config["strict"] or not self.strict_only

        if not self.run:
            return config

        known_words = self.config["known_words"]
        if isinstance(known_words, str):
            self.known_words |= set(Path(config["docs_dir"], known_words).read_text().splitlines())
        else:
            self.known_words |= set(known_words)

        self.backends = {}
        for backend_conf in self.backends_config:
            if isinstance(backend_conf, str):
                backend_name = backend_conf
                backend_config = {}
            else:
                backend_name, backend_config = next(iter(backend_conf.items()))
            self.backends[backend_name] = load_backend(backend_name)(
                known_words=self.known_words,
                config=backend_config,
            )

        return config

    def on_page_content(self, html: str, page: Page, **kwargs: Any) -> None:  # noqa: ARG002
        """Spell check everything.

        Hook for the [`on_page_content` event](https://www.mkdocs.org/user-guide/plugins/#on_page_content).

        Arguments:
            html: The HTML text.
            page: The page instance.
            **kwargs: Additional arguments passed by MkDocs.
        """
        if self.run and not any(fnmatch(page.file.src_path, pattern) for pattern in self.skip_files):
            words = get_words(
                html,
                known_words=self.known_words,
                min_length=self.min_length,
                max_capital=self.max_capital,
                ignore_code=self.ignore_code,
                allow_unicode=self.allow_unicode,
            )
            for word in words:
                for backend in self.backends.values():
                    backend.check(page, word)
