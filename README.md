# MkDocs SpellCheck

[![ci](https://github.com/pawamoy/mkdocs-spellcheck/workflows/ci/badge.svg)](https://github.com/pawamoy/mkdocs-spellcheck/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs-708FCC.svg?style=flat)](https://pawamoy.github.io/mkdocs-spellcheck/)
[![pypi version](https://img.shields.io/pypi/v/mkdocs-spellcheck.svg)](https://pypi.org/project/mkdocs-spellcheck/)
[![gitter](https://badges.gitter.im/join%20chat.svg)](https://app.gitter.im/#/room/#mkdocs-spellcheck:gitter.im)

A spell checker plugin for MkDocs.

This plugin can use different backends
to check the spelling of words in your final HTML pages.
These backends are:

- [`codespell`](https://github.com/codespell-project/codespell)
- [`symspellpy`](https://github.com/mammothb/symspellpy)

## Installation

To install all backends, use the `all` extra. Otherwise specify the name(s) of the backend(s) as extra.

```bash
pip install 'mkdocs-spellcheck[all]'
pip install 'mkdocs-spellcheck[codespell]'
pip install 'mkdocs-spellcheck[symspellpy]'
pip install 'mkdocs-spellcheck[codespell,symspellpy]'
```

## Usage

```yaml
# mkdocs.yml
plugins:
- search
- spellcheck:
    backends:  # the backends you want to use
    - symspellpy  # as strings
    - codespell:  # or nested configs
        dictionaries: [clear, rare]

    # known_words can also be a list of words
    known_words: known_words.txt

    # ignore words in <code> tags
    ignore_code: yes

    # minimum length of words to consider
    min_length: 2

    # maximum number of capital letters in a word
    max_capital: 1

    # keep unicode characters
    allow_unicode: no

    # skip files entirely (supports Unix shell-style wildcards)
    skip_files:
    - credits.md
    - coverage.md
    - reference/*

    # whether to only check in strict mode
    strict_only: yes
```

By default, the `symspellpy` backend is used.

Once your configuration is ready, just run `mkdocs build -s` to check the spelling inside your pages.

### `codespell`

The builtin dictionaries are:

- `clear` for unambiguous errors
- `rare` for rare (but valid) words that are likely to be errors
- `informal` for making informal words more formal
- `usage` for replacing phrasing with recommended terms
- `code` for words from code and/or mathematics that are likely
    to be typos in other contexts (such as `uint`)
- `names` for valid proper names that might be typos
- `en-GB_to_en-US` for corrections from `en-GB` to `en-US`
