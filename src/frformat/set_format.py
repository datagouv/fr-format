"""
A set format is a format that validates if a value is within a given set of
valid values.

This module introduces utilities to efficiently create new set formats :

- GenericSetFormat creates a validator with valid data passed on the fly
- `new` creates specialized versions where data is tied to the class
"""

from enum import Enum
from functools import total_ordering
from typing import FrozenSet, Generic, Type, TypeVar, Union, overload

from frformat import CustomStrFormat, Metadata
from frformat.common import normalize_value
from frformat.options import Options
from frformat.versioned_set import Version, VersionedSet


@total_ordering
class Millesime(Enum):
    """Millesime class implements the `Version` protocol methods."""

    M2023 = "2023"
    M2024 = "2024"
    LATEST = "latest"

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def __lt__(self, other) -> bool:
        return self.value < other.value

    def get_id(self) -> str:
        return self.value

    @classmethod
    def is_sorted(cls) -> bool:
        return True


class SingleSetFormat(CustomStrFormat):
    """This format defines a closed list of valid values"""

    _valid_values: FrozenSet = frozenset()
    """Dataset of valid values.

       Technical details:

       Beware, child classes may define an instance `_valid_values` attribute, which
       will always take precedence over the class attribute for the validation.
    """

    def __init__(self, options: Options = Options()):
        self._options = options

        normalized_extra_values = {
            normalize_value(e, self._options) for e in self._options.extra_valid_values
        }

        self._normalized_values = {
            normalize_value(e, self._options)
            for e in self._valid_values
            # in child classes, `self._valid_values` can reference an instance
            # attribute, if applicable ; otherwise the class attribute will
            # be used
        }.union(normalized_extra_values)

    def is_valid(self, value: str) -> bool:
        normalized_value = normalize_value(value, self._options)
        return normalized_value in self._normalized_values

    def get_valid_values_set(self) -> FrozenSet[str]:
        return self._valid_values


V = TypeVar("V", bound="Version")


class VersionedSetFormat(SingleSetFormat, Generic[V]):
    """This format defines a closed set of valid values, with different
    versions to choose from.

    Specific implementation details :

    - the type will hint at which version class to use for initializing the format validator.
    - a description of the format can be consulted with `MyClass.metadata.description` or at the top of `help(MyClass)`

    Technical details:

      - In the versioned set format, the `_valid_values` attribute is an instance attribute,
        which takes precedence over the class attribute of the mother class. The
        reason for this is that the exact valid values set is only known on instantiation.
    """

    _versioned_valid_values: VersionedSet = VersionedSet()

    def __init__(self, version: Union[V, str], options: Options = Options()):
        version_id = version if isinstance(version, str) else version.get_id()
        data = self._versioned_valid_values.get_data(version_id)
        if data is None:
            raise ValueError(f"No data available for version: {version_id}")

        self._valid_values = data
        super().__init__(options)


@overload
def new(
    class_name: str, name: str, description: str, valid_data: VersionedSet[V]
) -> Type[VersionedSetFormat[V]]: ...


@overload
def new(
    class_name: str, name: str, description: str, valid_data: FrozenSet
) -> Type[SingleSetFormat]: ...


def new(
    class_name: str,
    name: str,
    description: str,
    valid_data: Union[VersionedSet[V], FrozenSet[str]],
) -> Union[Type[VersionedSetFormat[V]], Type[SingleSetFormat]]:
    """Utility function to create a specialized version of a SetFormat.

    The returned class is a fully featured format that once initialized
    validates data passed as "valid_data" argument.

    If "valid_data" is a VersionedSet, the format will require the
    version to be specified at initialization.
    """
    if isinstance(valid_data, VersionedSet):

        class NewVersionedFormat(VersionedSetFormat):
            _versioned_valid_values = valid_data

        specialized_set_format = NewVersionedFormat

    else:

        class NewFormat(SingleSetFormat):
            _valid_values = valid_data

        specialized_set_format = NewFormat

    specialized_set_format.__name__ = class_name
    specialized_set_format.__qualname__ = class_name
    specialized_set_format.__doc__ = (
        f"{description}\n\n{specialized_set_format.__doc__}"
    )

    specialized_set_format.metadata = Metadata(name, description)

    return specialized_set_format
