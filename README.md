# Nighty Wheels

This repository contains code to build a bunch of lab-cosmo Python projects each
day, and make the pre-built wheels directly installable with pip.

## librascal

[![librascal](https://github.com/Luthaf/nightly-wheels/actions/workflows/rascal.yml/badge.svg?branch=main)](https://github.com/Luthaf/nightly-wheels/actions/workflows/rascal.yml)

Library to generate representations for atomic-scale learning, https://github.com/lab-cosmo/librascal

```bash
# install rascal dependencies first
pip install numpy scipy ase

# finally install librascal itself (this can not be a single step since there is
# another package called rascal on PyPI)
pip install --index-url https://luthaf.fr/nightly-wheels/ rascal
```

## equistore

Data storage and manipulation for atomistic machine learning, https://github.com/lab-cosmo/equistore

[![equistore](https://github.com/Luthaf/nightly-wheels/actions/workflows/equistore.yml/badge.svg?branch=main)](https://github.com/Luthaf/nightly-wheels/actions/workflows/equistore.yml)

```bash
# install the full project
pip install --extra-index-url https://luthaf.fr/nightly-wheels/ equistore

# install sub-packages (not required if you installed the full project)
pip install --extra-index-url https://luthaf.fr/nightly-wheels/ equistore-core
pip install --extra-index-url https://luthaf.fr/nightly-wheels/ equistore-operations
```


# Adding a new project

1. copy one of the workflow in `.github/workflows` to `<new-project.yml>` and
   edit it to build the wheels in the `build-wheels` job
2. open a PR with these changes, make sure CI passes and merge it
3. add the new project folder to the `index.html` file on the gh-pages branch
