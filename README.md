# Fr-format

A collection of validator to check data against french formats.

## Installation

The package is published on Pypi. Install with :

`pip install fr-format`

## Usage 

```python
from frformat import Departement

print(Departement.description())
Departement.is_valid("Haute-Vienne")
# True
Departement.is_valid("Canyon Cosmo")
# False
```

For better performance on big amount of data, use in conjunction with numpy.

## Available checks

Checkout [this file](./src/frformat/__init__.py) for a list of available validators.