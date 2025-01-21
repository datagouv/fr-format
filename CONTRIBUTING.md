# Contributing Guidelines

Thank you for taking the time to contribute to the `fr-format` project! Your help is greatly appreciated.

## How to Contribute ?

We welcome all forms of contributions: 

* Reporting issues or suggesting improvements
* Improving or adding documentation
* Enhancing code

In all cases, ensure you are working with the latest version of the project.

For more details, follow the sections below.

## Reporting issues or suggesting improvements

If you encounter a bug or have a suggestion, please:

1. Check if the issue already exists in the [Github Issues section](https://github.com/datagouv/fr-format/issues).
2. Provide a detailed issue report is very appreciated!\
   Including:\
              - A clear description of the problem or suggestion.\
              - Steps to reproduce the bug (if applicable).\
              - Any relevant logs or screenshots.

If you want to propose a new format, please verify:

1. that it does not already exists in the [list of available formats](./docs/formats.md)
2. that the new format is relevant. The scope of fr-format is _exclusively_ specifically French formats. 

See the [specific section](#implementing-a-new-french-format) below for guidelines on implementing a new format.

## Improving and adding documentation

All documentation files are located in [docs folder](./docs).\
Also, if you identify areas for improvement in the documentation, please contribute!

## Enhancing code

### Project setup and code style guidelines

See the [developper documentation](./docs/dev_documentation.md) for details on how to setup the project, and the code style guidelines.

### Adding features or fixing bugs

1. Create a fork of the repository.
2. Implement your changes and test them :
   - Run `make test` to execute tests.
   - Use `make lint` to ensure your code follows the project's style guidelines.
3. Document your changes:
   - Provide a clear explanation in your pull request description.
   - Add comments to your code if necessary.
   - If your changes include new features, please document them in the ["./docs"](./docs) folder. New formats' documentation are automatically generated (see below).
4. Finally, submit your pull request.

### Implementing a new French format

After verification, these are the steps to add it:

1. Create a new file in `src/frformat/formats` to implement the format validation logic. The most generic format interface is `CustomFormat`, but look out for helper functions (e.g. in `set_format.py`) for specific cases. (You can take examples from the existing code.)
2. Write tests for it!
3. Fix Linting problems running `make lint-fix`.
4. Import the format inside `./src/frformat/__init__` and add it to the `all_formats` list. 
5. Run `make generate-docs` to update the format documentation. 

## License

By contributing to `fr-format`, you agree that your contributions will be licensed under the project's [open-source license](./LICENSE.md).

Thank you for your contribution!
