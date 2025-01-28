# Fr-format

A collection of validators to check data against french formats.

## Installation

The package is published on PyPI. Install with :

`pip install frformat`

## Usage 

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

Check out [this documentantion](./docs/formats.md) that lists all available formats.

## Contributing

Found a bug, want to propose a feature or a new format? See the [contribution guidelines](./CONTRIBUTING.md) on how to proceed!


