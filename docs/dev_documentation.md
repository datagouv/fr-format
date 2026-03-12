# Developper documentation

This documentation is aimed at developpers that want to contribute or maintain fr-format.

## Setup the project

This project uses [uv](https://docs.astral.sh/uv/) as a dependency manager. 

Please follow these steps to contribute effectively to the project:

1. Clone the project repository and navigate to `fr-format` folder.
2. Insure you have uv installed by running `uv --version`. If not, [install uv](https://docs.astral.sh/uv/#installation).
3. Check your Python version matches the required version specified in `pyproject.toml`.
4. Run `uv sync --all-extras` to create a virtual environment and install all dependencies.

## Linting

Remember to format, lint, and sort imports with [Ruff](https://docs.astral.sh/ruff/) before committing (checks will remind you anyway):
```bash
ruff check --fix .
ruff format .
```

### Release

The release process uses the [`tag_version.sh`](/tag_version.sh) script to create git tags and update [CHANGELOG.md](/CHANGELOG.md) and [pyproject.toml](/pyproject.toml) automatically.

**Prerequisites**: [GitHub CLI](https://cli.github.com/) (`gh`) must be installed and authenticated, and you must be on the main branch with a clean working directory.

```bash
# Create a new release
./tag_version.sh <version>

# Example
./tag_version.sh 2.5.0

# Dry run to see what would happen
./tag_version.sh 2.5.0 --dry-run
```

The script automatically:
- Updates the version in `pyproject.toml`
- Extracts commits since the last tag and formats them for `CHANGELOG.md`
- Identifies breaking changes (commits with `!:` in the subject)
- Creates a git tag and pushes it to the remote repository
- Creates a GitHub release with the changelog content
