# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## [1.0.3](https://github.com/pawamoy/mkdocs-spellcheck/releases/tag/1.0.3) - 2024-03-23

<small>[Compare with 1.0.2](https://github.com/pawamoy/mkdocs-spellcheck/compare/1.0.2...1.0.3)</small>

### Code Refactoring

- Stop using deprecated API of `importlib.resources` ([0c96a56](https://github.com/pawamoy/mkdocs-spellcheck/commit/0c96a56b909fb8db8cc15bf98a2b84795987c3a8) by Stu Franks). [PR-19](https://github.com/pawamoy/mkdocs-spellcheck/pull/19), Co-authored-by: Timothée Mazzucotelli <dev@pawamoy.fr>

## [1.0.2](https://github.com/pawamoy/mkdocs-spellcheck/releases/tag/1.0.2) - 2023-09-05

<small>[Compare with 1.0.1](https://github.com/pawamoy/mkdocs-spellcheck/compare/1.0.1...1.0.2)</small>

### Bug Fixes

- Prevent loading of unused backends ([12062ff](https://github.com/pawamoy/mkdocs-spellcheck/commit/12062ffa7bb1ad4c66224ca63f1f036618076058) by Tobias Ahrens). [PR #17](https://github.com/pawamoy/mkdocs-spellcheck/pull/17)

## [1.0.1](https://github.com/pawamoy/mkdocs-spellcheck/releases/tag/1.0.1) - 2023-08-19

<small>[Compare with 1.0.0](https://github.com/pawamoy/mkdocs-spellcheck/compare/1.0.0...1.0.1)</small>

### Bug Fixes

- Remove `'s` from possessive nouns for spellcheck ([1f11985](https://github.com/pawamoy/mkdocs-spellcheck/commit/1f11985532e9fda547ac25a1f6b57a77bdeba46c) by Stu Franks). [PR #16](https://github.com/pawamoy/mkdocs-spellcheck/pull/16)
- Retain single quotes that are part of words ([8dd8206](https://github.com/pawamoy/mkdocs-spellcheck/commit/8dd8206eaccc709463873eef768fde45b360be26) by Stu Franks). [PR #16](https://github.com/pawamoy/mkdocs-spellcheck/pull/16)

### Code Refactoring

- Stop using deprecated warning filter ([ae3a584](https://github.com/pawamoy/mkdocs-spellcheck/commit/ae3a584229523087c21f77a6a74e14986d5fc8be) by Timothée Mazzucotelli).

## [1.0.0](https://github.com/pawamoy/mkdocs-spellcheck/releases/tag/1.0.0) - 2022-11-24

<small>[Compare with 0.2.2](https://github.com/pawamoy/mkdocs-spellcheck/compare/0.2.2...1.0.0)</small>

### Breaking Changes

You must now specify an extra when installing `mkdocs-spellcheck`:

```
pip install mkdocs-spellcheck[all]         # install all spelling backends
pip install mkdocs-spellcheck[codespell]   # detects common mistakes
pip install mkdocs-spellcheck[symspellpy]  # uses the english dictionary
```

### Features
- Add option to run only when strict mode is enabled ([d6520d9](https://github.com/pawamoy/mkdocs-spellcheck/commit/d6520d93483fe5e50b123692d3e269d2c0630235) by Timothée Mazzucotelli). [PR #15](https://github.com/pawamoy/mkdocs-spellcheck/issues/15)
- Add `codespell` backend ([bc8e84c](https://github.com/pawamoy/mkdocs-spellcheck/commit/bc8e84caebbf88d707dfcc4d2f9116444d7b01c6) by Timothée Mazzucotelli). [Issue #11](https://github.com/pawamoy/mkdocs-spellcheck/issues/11)


## [0.2.2](https://github.com/pawamoy/mkdocs-spellcheck/releases/tag/0.2.2) - 2022-11-02

<small>[Compare with 0.2.1](https://github.com/pawamoy/mkdocs-spellcheck/compare/0.2.1...0.2.2)</small>

### Bug Fixes
- Correctly reset HTML stripper state after code block ([3db4add](https://github.com/pawamoy/mkdocs-spellcheck/commit/3db4addd5553083d12f48c8dd41873da01ce48f9) by Timothée Mazzucotelli). [Issue #13](https://github.com/pawamoy/mkdocs-spellcheck/issues/13)


## [0.2.1](https://github.com/pawamoy/mkdocs-spellcheck/releases/tag/0.2.1) - 2022-04-11

<small>[Compare with 0.2.0](https://github.com/pawamoy/mkdocs-spellcheck/compare/0.2.0...0.2.1)</small>

### Bug Fixes
- Prevent words concatenation ([06d36a2](https://github.com/pawamoy/mkdocs-spellcheck/commit/06d36a2a4fb9f93d92b006dfe2763a544f8f842a) by Timothée Mazzucotelli). [Issue #9](https://github.com/pawamoy/mkdocs-spellcheck/issues/9)
- Warn even when there are no suggestions ([f6621f6](https://github.com/pawamoy/mkdocs-spellcheck/commit/f6621f6e87a7974d15d21312ee4b9b803372eb89) by Timothée Mazzucotelli). [Issue #12](https://github.com/pawamoy/mkdocs-spellcheck/issues/12)


## [0.2.0](https://github.com/pawamoy/mkdocs-spellcheck/releases/tag/0.2.0) - 2022-01-29

<small>[Compare with 0.1.1](https://github.com/pawamoy/mkdocs-spellcheck/compare/0.1.1...0.2.0)</small>

### Features
- Add `max_capital` option ([be3d48e](https://github.com/pawamoy/mkdocs-spellcheck/commit/be3d48e50b4e26219e8a33a399c3f8eeac440c22) by Timothée Mazzucotelli). [Issue #2](https://github.com/pawamoy/mkdocs-spellcheck/issues/2)

### Code Refactoring
- Don't consider words containing digits ([42d42f1](https://github.com/pawamoy/mkdocs-spellcheck/commit/42d42f16e565ec123be61061f54d1867f32de9a6) by Timothée Mazzucotelli). [Issue #1](https://github.com/pawamoy/mkdocs-spellcheck/issues/1)


## [0.1.1](https://github.com/pawamoy/mkdocs-spellcheck/releases/tag/0.1.1) - 2022-01-25

<small>[Compare with 0.1.0](https://github.com/pawamoy/mkdocs-spellcheck/compare/0.1.0...0.1.1)</small>

### Code Refactoring
- Prefix logs with package name only ([7ea8ad9](https://github.com/pawamoy/mkdocs-spellcheck/commit/7ea8ad93dc0621f6c386b8928ba3b046bedfbe3e) by Timothée Mazzucotelli).


## [0.1.0](https://github.com/pawamoy/mkdocs-spellcheck/releases/tag/0.1.0) - 2022-01-25

<small>[Compare with first commit](https://github.com/pawamoy/mkdocs-spellcheck/compare/4b2335e8caa3956fb6fd7c31a4473ea0e21e4e15...0.1.0)</small>

### Build
- Depend on `symspellpy` ([2dc1633](https://github.com/pawamoy/mkdocs-spellcheck/commit/2dc1633668da64438b63058cdcb091a6a48c3411) by Timothée Mazzucotelli).
- Fix pyproject ([9f9dc0d](https://github.com/pawamoy/mkdocs-spellcheck/commit/9f9dc0d55831c0694fa01f620524faa88d9ee147) by Timothée Mazzucotelli).

### Code Refactoring
- Clean up ([e7c0e46](https://github.com/pawamoy/mkdocs-spellcheck/commit/e7c0e46c6c73fdbdf1a91d37fb544a63d3651006) by Timothée Mazzucotelli).
- Remove useless files ([4e85cd0](https://github.com/pawamoy/mkdocs-spellcheck/commit/4e85cd0a222dc29443b649ef34a3533163faa63e) by Timothée Mazzucotelli).

### Features
- Implement spell check plugin ([3a1367b](https://github.com/pawamoy/mkdocs-spellcheck/commit/3a1367b9a5ebd04ee44d8591119e00be67a2410a) by Timothée Mazzucotelli).
- Generate project using pawamoy/copier-pdm template ([4b2335e](https://github.com/pawamoy/mkdocs-spellcheck/commit/4b2335e8caa3956fb6fd7c31a4473ea0e21e4e15) by Timothée Mazzucotelli).
