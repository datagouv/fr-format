# Fr-format

The standard library `fr-format` provides a collection of validators to check data against typical French formats.

It has been initially developed for sharing validation functions between these two projects:

* [validata](https://gitlab.com/validata-table)
* [csv-detective](https://github.com/datagouv/csv-detective)

## Available formats

Check out [this documentantion](./docs/formats.md) that lists all available formats.

## Installation

The package is published on PyPI. Install with :

`pip install frformat`

## Usage 

**User story**

As a `fr-format` user, specifically a developer or data scientist, you may need to validate a value according to a given French format. This feature enables you to easily verify whether your data  is valid or not.\
Additionally, this project allows you to retrieve the entire set of valid values when applicable. For example, this can be useful in a frontend to display the complete set (e.g. in a dropdown menu).

Here's an example of how to use fr-format:
```python
from frformat import Departement, Options, Millesime

print(Departement.description())

_options = Options(
    ignore_case=True,
    ignore_accents=True,
    ignore_extra_whitespace=True
)
Departement(Millesime.LATEST, _options).is_valid("haute-vienne")
# True
Departement(Millesime.M2023, _options).is_valid("Canyon Cosmo")
# False
```
For more details, consult the [Options](./src/frformat/options.py) data class.

For better performance on big amounts of data, use in conjunction with numpy.

## Contributing

Found a bug, want to propose a feature or a new format? See the [contribution guidelines](./CONTRIBUTING.md) on how to proceed!

