
# Developping tools

## Dependency manager

This project uses [poetry](https://python-poetry.org/) as a dependency 
manager. 

```
pip install poetry
```

## Developping environment

### Linting

Install developper tools with :

```
poetry install --with linting
```

Code style is checked continuously and enforced with 
[`black`](https://github.com/psf/black), 
[`isort`](https://pypi.org/project/isort/), 
[`flake8`](https://pypi.org/project/flake8/) and 
[`pyright`](https://github.com/microsoft/pyright).

### Task Runner

The project uses a Makefile to manage common tasks. The command `make` will show available tasks.

## Publishing process

This project uses git tags associated with [continuous 
deployment](../../.github/workflows/publish.yaml) to manage version bumps and 
Pypi publication. 

Here is the full process to publish a new version :

- Check which version to publish. We use [semantic 
  versionning](https://semver.org/).
- `git checkout main && git pull`
- Update [CHANGELOG.md](../../CHANGELOG.md) and push changes on main.
- `git tag vX.Y.Z`
- `git push --tags`
- Check that CD pipeline has succeeded



