modern_python
=========

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.12684030.svg)](https://doi.org/10.5281/zenodo.12684030)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.12684157.svg)](https://doi.org/10.5281/zenodo.12684157)

This repository serves as inspiration/template for setting up your own modern python project.
It uses [hatch](https://hatch.pypa.io/latest/) as a project manager.
`hatch` sets up a virtual environment, installs the correct Python version, downloads and installs the dependencies, and runs the program.
For a more comprehensive description, see below.

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

