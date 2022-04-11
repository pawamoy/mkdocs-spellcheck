# MkDocs SpellCheck

[![ci](https://github.com/pawamoy/mkdocs-spellcheck/workflows/ci/badge.svg)](https://github.com/pawamoy/mkdocs-spellcheck/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://pawamoy.github.io/mkdocs-spellcheck/)
[![pypi version](https://img.shields.io/pypi/v/mkdocs-spellcheck.svg)](https://pypi.org/project/mkdocs-spellcheck/)
[![gitpod](https://img.shields.io/badge/gitpod-workspace-blue.svg?style=flat)](https://gitpod.io/#https://github.com/pawamoy/mkdocs-spellcheck)
[![gitter](https://badges.gitter.im/join%20chat.svg)](https://gitter.im/mkdocs-spellcheck/community)

A spell checker plugin for MkDocs.

## Installation

```bash
pip install mkdocs-spellcheck
```

## Usage

```yaml
# mkdocs.yml
plugins:
- search
- spellcheck:
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

    # skip files entirely
    skip_files:
    - credits.md
    - coverage.md
```
