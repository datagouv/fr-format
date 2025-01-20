# Contributing Guidelines

Thank you for taking the time to contribute to the `fr-format` project! Your help is greatly appreciated.

## How to Contribute ?

We welcome all forms of contributions,they are highly encouraged: 

* Submitting Pull Requests (Enhancing code, Improving or adding documentation)
* Reporting Issues or suggesting improvements

For more details, follow the sections below.

### Submitting Pull Requests

#### Enhancing code

Please follow these important steps to contribute effectively to the project:

1. Clone the project repository and navigate to `fr-format` folder.
2. Insure you have Poetry installed by running `poetry --version`. If not, [install Poetry](https://pypi.org/project/poetry/).
3. Check your Python version matches the required version specified in `pyproject.toml`.
4. Run `poetry install` to create a virtual environment and install all dependencies.
5. Activate the virtual environment using `poetry shell`.
6. Use the `Makefile` for predefined tasks. Run `make help` to see available commands.

##### Adding features or fixing bugs

At first, ensure you are working with the latest version of the project: `git pull origin main`.

After verification, follow these steps: 

1. Create a new branch for your feature or fix: `git checkout -b feature-name`.
2. Implement your changes and test them :
   - Run `make test` to execute tests.
   - Use `make lint` to ensure your code follows the project's style guidelines.
3. Document your changes:
   - Provide a clear explanation in your pull request description.
   - Add comments to your code if necessary. 
 
6. Finally, submit your pull request and tag relevant contributors for review .

##### Suggesting a new french format (Main feature)

Before adding a new format, please verify at first these two points before creating the pull request appropriate to this feature:

1. Check the [list of available formats](./docs/formats.md) to ensure it doesn't already exist.
2. Be sure that the new format is relevant, meaningful and specifically French. 

After verification, these are the steps to add it:

1. Create a file to store validated data values(If the data list is large)
2. Create a second one to implement the format validation logic. (You can take examples from the existing code)
3. Test it!
4. Fix Linting problems running `make lint-fix`.
5. Import the format inside `./src/frformat/__init__`.
6. Add it to `all_formats` list. 
7. Run `make generate-docs` to update the format documentation. 
The aim of this step is to save all formats inside one table to be more clear for users.

#### Improving and adding documentation

All documentation files are located in [docs folder](./docs).\
If your changes include complex logic or functionality, add clear and concise doc comments to explain them.
Also, if you identify areas for improvement in the [README file](./docs/dev/README.md), other documentation files, or even files without existing documentation where an explanation would add value, please contribute, it's highly encouraged!

**Note**: If you are adding a new french format to the project, remember to run `make generate-docs` to update the documentation and refresh the list of all available formats.

### Reporting Issues or suggesting improvements

If you encounter a bug or have a suggestion, please:

1. Ensure you are using the latest version of the project and verify if updating fixes your issue first.
2. Check if the issue already exists in the [Github Issues section](https://github.com/datagouv/fr-format/issues) (please do not open a duplicate one !).
3. Provide a detailed issue report is very appreciate!\
   Including:\
              - A clear description of the problem or suggestion.\
              - Steps to reproduce the bug (if applicable).\
              - Any relevant logs or screenshots.

## Code Style Guidelines

`fr format` projevt uses the following linting and formatting dependencies:
- [Black](https://black.readthedocs.io/en/stable/)
- [Isort](https://pycqa.github.io/isort/)
- [Flake8](https://flake8.pycqa.org/)
- [Pyright](https://github.com/microsoft/pyright)

These tools are installed automatically when you run `poetry install` after forking the project.\
Before submitting your code, run `make lint` to check for linting issues and fix them using `make lint-fix`.

## License

By contributing to `fr-format`, you agree that your contributions will be licensed under the project's open-source license: MIT.

Thank you for your contribution !



