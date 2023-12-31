# PackTest Beet Plugin

[![GitHub Actions](https://github.com/CarbonSmasher/packtest_beet/workflows/CI/badge.svg)](https://github.com/CarbonSmasher/packtest_beet/actions)
[![PyPI](https://img.shields.io/pypi/v/packtest_beet.svg)](https://pypi.org/project/packtest_beet/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/packtest_beet.svg)](https://pypi.org/project/packtest_beet/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Discord](https://img.shields.io/discord/900530660677156924?color=7289DA&label=discord&logo=discord&logoColor=fff)](https://discord.gg/98MdSGMm8j)

## Introduction

Load and run PackTest tests in your beet project

## Installation

The package can be installed with `pip`.

```bash
$ pip install packtest_beet
```

## Contributing

Contributions are welcome. Make sure to first open an issue discussing the problem or the new feature before creating a pull request. The project uses [`poetry`](https://python-poetry.org).

```bash
$ poetry install
```

You can run the tests with `poetry run pytest`.

```bash
$ poetry run pytest
```

The project must type-check with [`pyright`](https://github.com/microsoft/pyright). If you're using VSCode the [`pylance`](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) extension should report diagnostics automatically. You can also install the type-checker locally with `npm install` and run it from the command-line.

```bash
$ npm run watch
$ npm run check
```

The code follows the [`black`](https://github.com/psf/black) code style. Import statements are sorted with [`isort`](https://pycqa.github.io/isort/).

```bash
$ poetry run isort packtest_beet examples tests
$ poetry run black packtest_beet examples tests
$ poetry run black --check packtest_beet examples tests
```

---

License - [MIT](https://github.com/CarbonSmasher/packtest_beet/blob/main/LICENSE)
