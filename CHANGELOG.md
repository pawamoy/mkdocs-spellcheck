# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
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
