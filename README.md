# Fr-format

A collection of validators to check data against french formats.

## Installation

The package is published on PyPI. Install with :

`pip install frformat`

## Usage 

```python
from frformat import Departement

print(Departement.description())
Departement.is_valid("Haute-Vienne")
# True
Departement.is_valid("Canyon Cosmo")
# False
```

For better performance on big amounts of data, use in conjunction with numpy.

## Available checks

Checkout [this file](./docs/output_validator_list.md) for a list of available validators.
