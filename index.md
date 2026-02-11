# MkDocs SpellCheck

> [!WARNING] This project is in maintenance mode. I'm now dedicating my time to [Zensical](https://zensical.org/). Feel free to reach out for a responsible transfer of maintainership.

A spell checker plugin for MkDocs.

This plugin can use different backends to check the spelling of words in your final HTML pages. These backends are:

- [`codespell`](https://github.com/codespell-project/codespell)
- [`symspellpy`](https://github.com/mammothb/symspellpy)

## Installation

To install all backends, use the `all` extra. Otherwise specify the name(s) of the backend(s) as extra.

```
pip install 'mkdocs-spellcheck[all]'
pip install 'mkdocs-spellcheck[codespell]'
pip install 'mkdocs-spellcheck[symspellpy]'
pip install 'mkdocs-spellcheck[codespell,symspellpy]'
```

## Usage

```
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
- `code` for words from code and/or mathematics that are likely to be typos in other contexts (such as `uint`)
- `names` for valid proper names that might be typos
- `en-GB_to_en-US` for corrections from `en-GB` to `en-US`

### On-off regions

In some situations it can be useful to temporarily disable spell checking for a document. To this end, MkDocs SpellCheck recognizes special guards `mkdocs-spellcheck-{on,off}`:

```
Here MkDocs SpellCheck checks for correct spelling.

<!-- mkdocs-spellcheck-off -->
In this block it doesn't.
<!-- mkdocs-spellcheck-on -->

Here spelling checks are performed again.
```

## Sponsors

**Silver sponsors**

**Bronze sponsors**

______________________________________________________________________

*And 7 more private sponsor(s).*
