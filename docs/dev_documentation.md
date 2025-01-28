# Developper documentation

This documentation is aimed at developpers that want to contribute or maintain fr-format.

## Setup the project

This project uses [poetry](https://python-poetry.org/) as a dependency manager. 

Please follow these steps to contribute effectively to the project:

1. Clone the project repository and navigate to `fr-format` folder.
2. Insure you have Poetry installed by running `poetry --version`. If not, [install Poetry](https://pypi.org/project/poetry/).
3. Check your Python version matches the required version specified in `pyproject.toml`.
4. Run `poetry install --all-groups` to create a virtual environment and install all dependencies.
5. Activate the virtual environment using `poetry shell`.

## Task Runner

The project uses a Makefile to manage common tasks. The command `make` or `make help` will show available tasks.

## Code Style Guidelines

`fr format` project uses the following linting and formatting dependencies:

- [black](https://black.readthedocs.io/en/stable/)
- [isort](https://pycqa.github.io/isort/)
- [flake8](https://flake8.pycqa.org/)
- [pyright](https://github.com/microsoft/pyright)

These tools are can be installed with the `linting` group (`poetry install --with linting`).

## Publishing process

This project uses git tags associated with [continuous deployment](../.github/workflows/publish.yaml) to manage version bumps and Pypi publication. 

Here is the full process to publish a new version :

- Check which version to publish. We use [semantic versionning](https://semver.org/).
- `git checkout main && git pull`
- Update [CHANGELOG.md](../CHANGELOG.md) and push changes on main.
- `git tag vX.Y.Z`
- `git push --tags`
- Check that CD pipeline has succeeded



