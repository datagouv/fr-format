# Fr-format

The standard library `fr-format` has been developed for sharing validation functions between these two projects for now:

* [validata](https://gitlab.com/validata-table)
* [csv-detective](https://github.com/datagouv/csv-detective)

It provides a collection of validators to check data against typical French formats.

## Usage

## Installation

The package is published on PyPI. Install with :

`pip install frformat`

## Usage 

**User story**

As a fr-format user, you want to validate a value according to a given French format. This allows you to easily check if the data provided by your project users is valid or not .

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

## Available formats

Check out [this file](./docs/formats.md) for a list of available formats.
