modern_python
=========

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.12684157.svg)](https://doi.org/10.5281/zenodo.12684157)


Contents
-----------------
- [Overview](#overview)
- [How to use](#how-to-use)
- [Attribution](#attribution)

## Overview

This repository serves as a template for setting up Python3-based (research software) projects in a modern way. This includes:

- A directory structure appropriate for package installation and publishing via e.g. PyPI
- Metadata files following community guidelines (Readme, License, Code of Conduct, Changelog, Citation file)
- Pre-commit setup enforcing linting
- Minimal CI/CD (Continuous Integration) using GitHub Actions
- A pre-formatted logger

This template has been set up for use in the [Medema group](https://github.com/medema-group), but is also generally applicable.
Sections that specifically address members of the Medema group are marked with a **{Medema-Group}** tag.

To see how you can adopt this template for your project, see next section.

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

Let's install your package with `uv` and do a test-run:

```commandline
uv sync
uv run python src/your_cool_project/main.py
```

You should see a logging message saying `Hello, world`.

If you see errors, it is likely that you did not rename the `src/your_cool_project` folder according to the newly chosen name for your project

### 3. Set up `pre-commit`

Once your project is installed, you can set up `pre-commit`. 
This small helper program runs a suite of additional tools to lint your code, perform checks, and run tests **BEFORE** you commit your code.
You can adjust the programs by editing [.pre-commit-config](./.pre-commit-config.yaml) or changing their settings in the [pyproject.toml](./pyproject.toml) file.

To set up `pre-commit`, run:

```commandline
uv run pre-commit install
```

From now on, checks will run on every commit. 
You can override the checks with `git commit -m "<your message>" --no-verify`.


### 4. Adjust the metadata files

Now that the basics are set up, it is time to adjust the metadata files. 
These are extremely important from the perspective of research software following FAIR (Findable, Accessible, Interoperable, Reusable) principles.

#### README

The `README` file is the main documentation for your repository.
A well-crafted `README` will present the most important aspects at one glance and facilitate interaction with your code.

##### TO DO

- [ ] Adjust the [README_TEMPLATE](./README_TEMPLATE.md) to your needs and replace the current `README`.

#### LICENSE

A `LICENSE` file specifies under which conditions people can use the research software. 
A repository without `LICENSE` file can't be reasonably used.

While there are many licenses available, the most common types are [CC BY NC](https://creativecommons.org/licenses/by-nc/4.0/deed), [CC BY](https://creativecommons.org/licenses/by/4.0/deed.en), and [CC0 (public domain)](https://creativecommons.org/public-domain/cc0/).
In the **{Medema-Group}**, we usually use a CC BY license that is compatible with the WUR guidelines, such as the [MIT](https://opensource.org/license/mit) or the [Apache 2.0](https://opensource.org/license/apache-2-0) licenses.
For instance, this template is licensed using the `UNLICENSE` (a type of `CC0`), allowing free use without crediting the creator.

If you are unsure what to pick, you can consult [this handy license picker](https://creativecommons.org/chooser/).

##### TO DO

- [ ] Replace the current `LICENSE` file with one of your choosing.

#### CITATION

In most cases, you want others to cite your work. 
To facilitate this, it is common practice to include a [CITATION.cff](./CITATION.cff) file.
This file specifies to whom credit is due, and also allows to cross-reference journal articles.

You can easily create your own `CITATION.cff` file using [CFF INIT](https://citation-file-format.github.io/cff-initializer-javascript/#/).

##### TO DO

- [ ] Replace the current dummy `CITATION.cff` file with your own.

##### CHANGELOG

[Keeping a changelog](https://keepachangelog.com/en/1.1.0/) is essential for letting people know what has changed between versions.
Nobody likes to look at Git commit messages to figure out why their code does not work anymore.





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

