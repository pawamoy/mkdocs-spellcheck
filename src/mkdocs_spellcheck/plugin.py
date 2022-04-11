"""
MkDocs SpellCheck package.

A spell checker plugin for MkDocs.
"""

from __future__ import annotations

from importlib import resources
from pathlib import Path

from mkdocs.config import Config
from mkdocs.config.config_options import Type as MkType
from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page
from symspellpy import SymSpell, Verbosity

from mkdocs_spellcheck.loggers import get_logger
from mkdocs_spellcheck.words import get_words

logger = get_logger(__name__)


class SpellCheckPlugin(BasePlugin):
    """A `mkdocs` plugin.

    This plugin defines the following event hooks:

    - `on_config`
    - `on_page_content`

    Check the [Developing Plugins](https://www.mkdocs.org/user-guide/plugins/#developing-plugins) page of `mkdocs`
    for more information about its plugin system.
    """

    config_scheme: tuple[tuple[str, MkType], ...] = (
        ("known_words", MkType((str, list), default=[])),
        ("skip_files", MkType(list, default=[])),
        ("min_length", MkType(int, default=2)),
        ("max_capital", MkType(int, default=1)),
        ("ignore_code", MkType(bool, default=True)),
        ("allow_unicode", MkType(bool, default=False)),
    )

    def __init__(self) -> None:  # noqa: D107
        self.known_words: set[str] = set()
        self.spell: SymSpell = None
        super().__init__()

    def on_config(self, config: Config, **kwargs) -> Config:
        """Load words to ignore.

        Hook for the [`on_config` event](https://www.mkdocs.org/user-guide/plugins/#on_config).

        Arguments:
            config: The MkDocs config object.
            kwargs: Additional arguments passed by MkDocs.

        Returns:
            The modified config.
        """
        self.skip_files = self.config["skip_files"]
        self.min_length = self.config["min_length"]
        self.max_capital = self.config["max_capital"]
        self.ignore_code = self.config["ignore_code"]
        self.allow_unicode = self.config["allow_unicode"]

        known_words = self.config["known_words"]
        if isinstance(known_words, str):
            self.known_words |= set(Path(config["docs_dir"], known_words).read_text().splitlines())
        else:
            self.known_words |= set(known_words)

        self.spell = SymSpell()
        with resources.path("symspellpy", "frequency_dictionary_en_82_765.txt") as dictionary_path:
            self.spell.load_dictionary(dictionary_path, 0, 1)
        return config

    def on_page_content(self, html: str, page: Page, **kwargs) -> None:
        """Spell check everything.

        Hook for the [`on_page_content` event](https://www.mkdocs.org/user-guide/plugins/#on_page_content).

        Arguments:
            html: The HTML text.
            page: The page instance.
            kwargs: Additional arguments passed by MkDocs.
        """
        if page.file.src_path not in self.skip_files:
            words = get_words(
                html,
                known_words=self.known_words,
                min_length=self.min_length,
                max_capital=self.max_capital,
                ignore_code=self.ignore_code,
                allow_unicode=self.allow_unicode,
            )
            for word in words:
                suggestions = self.spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)
                if suggestions:
                    candidates = "', '".join(suggestion.term for suggestion in suggestions if suggestion.term != word)
                    if candidates:
                        logger.warning(f"{page.file.src_path}: Misspelled '{word}', did you mean '{candidates}'?")
                else:
                    logger.warning(f"{page.file.src_path}: Misspelled '{word}', no suggestions")
