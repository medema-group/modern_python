modern_python
=========

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.12684157.svg)](https://doi.org/10.5281/zenodo.12684157)


Contents
-----------------
- [Overview](#overview)
- [How to use](#how-to-use)
- [Attribution](#attribution)

## Overview

This repository serves as a template for setting up Python3-based projects in a modern way. This includes:

- A directory structure appropriate for package installation and publishing via e.g. PyPI
- Metadata files following community guidelines (Readme, License, Code of Conduct, Changelog, Citation file)
- Pre-commit setup enforcing linting
- Minimal CI/CD (Continuous Integration) using GitHub Actions
- A pre-formatted logger

To see how you can adopt this template for your project, see next section

## How to use

*Nota bene: this template assumes that you have the `uv` package manager installed. To install `uv`, check out [their documentation](https://docs.astral.sh/uv/getting-started/installation/)*

This is a step-by-step guide how to adopt this template for your project. Let's start!

### 1. Describe your project

Every project should start with setting up its metadata, such as name, authors, required Python version, packages, etc.
In a modern Python project, a [pyproject.toml](./pyproject.toml) file is used to store this information. 
Additionally, this file also serves as a "recipe" to install your package (more about that later).

First, lets modify the [pyproject.toml](./pyproject.toml) file:

- Adjust the `name` and rename the directory `src/your_cool_project` to your chosen name.
- Decide on a versioning system (the default [Semantic Versioning](https://semver.org/) is highly recommended). Set the `version` to `0.1.0` - this is the only place you will set the version.
- Add a `description`.
- Depending on your needs, update the dependencies. Consider [pinning](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) your dependencies.

### 2. Install your project

Your Python project should be easily installable, to ensure that it is portable. 
Currently, the best package manager is `uv`: lightweight and extremely fast. 
`uv` will create a virtual environment (to keep your packages from messing up your OS) and install your packages.
Importantly, it will also set up a `uv.lock` lockfile, which specifies all your packages *and the packages your packages rely on*, making your installation truly reproducible. 

Let`s install your package with `uv` and do a test-run:

```commandline
uv sync
uv run python src/your_cool_project/main.py
```

You should see a logging message saying `Hello, world`.

If you see errors, it is likely that you did not rename the `src/your_cool_project` folder accoding to the newly chosen name for your project

### 3. Adjust the metadata files



### TODO: continue here


## Installation

### For users

- Install `python3`
- Install `hatch` using one of the methods described [here](https://hatch.pypa.io/1.12/install/)
- Download or clone this repository
- Run `hatch -v env create`

### For developers

- Install `python3`
- Install `hatch` using one of the methods described [here](https://hatch.pypa.io/1.12/install/)
- Download or clone this repository
- Run `hatch -v env create dev`. This will download and install the appropriate Python version and any required packages
- Run `hatch run dev:pre-commit install`. This will set up `pre-commit`

## Quick Start

### For users

- `hatch run modern_python`

### For developers

- `hatch run dev:modern_python`

## Remove package

### For users

- `hatch env remove`

### For developers

- `hatch env remove dev`

## Background

Python3 is one of most popular languages in scientific programming.
While its flexible syntax is great for beginners, this can become a issue for larger projects.
Therefore, the community has started to adopt a number of best practices to make working on larger, multi-person projects more convenient.
Some of these best practices have been incorporated in auxiliary programs (from here: 'plugins') that provide capabilities **linting**, **formatting**, **type hinting**, and **testing**.

### What is included in this repo?

- A basic project directory structure with some placeholder Python files (`modern_python`, `tests`)
- A set of standard files (in capital letters, e.g. LICENSE, CHANGELOG) for metadata about the repository
- A `pyproject.toml` file that manages metadata, versioning, dependencies, environments, and plugins. This file is also used by `hatch` for setting up environments (`default`, `dev`), download and installation of dependencies.
- A `.pre-commit-config.yaml` file that manages the plugins for linting (`ruff-check`), formatting (`ruff-format`), type hinting (`mypy`), and testing (`pytest`). If `pre-commit` is activated, this suite of programs is performed with each `git commmit`.

### Who is this repo not for?

For Python projects not in version control (e.g. single-use scripts), such an advanced setup is likely not necessary. 
However, once a project becomes more elaborate, it is often useful to give it at least a minimum of formalism.
This repo can help to reduce the time to do so, since it only requires a minimum of adaption.

