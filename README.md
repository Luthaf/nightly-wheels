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

## metatensor

[![metatensor](https://github.com/Luthaf/nightly-wheels/actions/workflows/metatensor.yml/badge.svg?branch=main)](https://github.com/Luthaf/nightly-wheels/actions/workflows/metatensor.yml)

Data storage and manipulation for atomistic machine learning, https://github.com/lab-cosmo/metatensor

```bash
# install the full project
pip install --extra-index-url https://luthaf.fr/nightly-wheels/ metatensor
# install the full project, including the torch interface
pip install --extra-index-url https://luthaf.fr/nightly-wheels/ metatensor[torch]

# install sub-packages (not required if you installed the full project)
pip install --extra-index-url https://luthaf.fr/nightly-wheels/ metatensor-core
pip install --extra-index-url https://luthaf.fr/nightly-wheels/ metatensor-torch
pip install --extra-index-url https://luthaf.fr/nightly-wheels/ metatensor-operations
```

## rascaline

[![rascaline](https://github.com/Luthaf/nightly-wheels/actions/workflows/rascaline.yml/badge.svg?branch=main)](https://github.com/Luthaf/nightly-wheels/actions/workflows/rascaline.yml)

Computing representations for atomistic machine learning, https://github.com/luthaf/rascaline

```bash
# install the full project
pip install --extra-index-url https://luthaf.fr/nightly-wheels/ rascaline
```

# Adding a new project

1. copy one of the workflow in `.github/workflows` to `<new-project.yml>` and
   edit it to build the wheels in the `build-wheels` job
2. open a PR with these changes, make sure CI passes and merge it
3. add the new project folder to the `index.html` file on the gh-pages branch
