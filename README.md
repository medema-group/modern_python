modern_python
=========

This repository serves as inspiration/template for setting up your own modern python project.

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