"""
A set format is a format that validates if a value is within a given set of
valid values.

This module introduces utilities to efficiently create new set formats.
"""

from enum import Enum
from functools import total_ordering
from typing import FrozenSet, Type, Union

from frformat import CustomStrFormat, Metadata
from frformat.common import normalize_value
from frformat.options import Options
from frformat.versioned_set import VersionedSet


@total_ordering
class Millesime(Enum):
    """Millesime class implements the `Version` protocol methods"""

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


class GenericSetFormat(CustomStrFormat):
    """A format that checks if a value is among a set of valid values.

    In the generic version, valid data is passed at object initialisation.

    See the `new` function to create a specialized version with the valid data
    set tied to the class.
    """

    def __init__(self, valid_data: FrozenSet, options: Options = Options()):
        self._options = options
        self._data = valid_data

        normalized_extra_values = {
            normalize_value(e, self._options) for e in self._options.extra_valid_values
        }

        self._normalized_values = {
            normalize_value(e, self._options) for e in self._data
        }.union(normalized_extra_values)

    def is_valid(self, value: str) -> bool:
        normalized_value = normalize_value(value, self._options)
        return normalized_value in self._normalized_values


def new(
    class_name: str,
    name: str,
    description: str,
    valid_data: Union[VersionedSet, FrozenSet[str]],
) -> Type:
    """Utility function to create a specialized version of a SetFormat.

    The returned class is a fully featured format that once initialized
    validates data passed as "valid_data" argument.

    If "valid_data" is a VersionnedSet, the format will require the
    version to be specified at initialization.
    """
    if isinstance(valid_data, VersionedSet):

        class VersionnedSetFormat(GenericSetFormat):
            def __init__(
                self, cog: Union[Millesime, str], options: Options = Options()
            ):
                try:
                    cog = Millesime(cog)
                except ValueError:
                    raise ValueError(f"Invalid cog parameter: {cog}")
                data = valid_data.get_data(cog.get_id())
                if data is None:
                    raise ValueError(
                        f"No data available for geographical code: {cog.value}"
                    )

                super().__init__(data, options)

        specialized_set_format = VersionnedSetFormat

    else:

        class SingleSetFormat(GenericSetFormat):
            def __init__(self, options: Options = Options()):
                super().__init__(valid_data, options)

        specialized_set_format = SingleSetFormat

    specialized_set_format.__name__ = class_name
    specialized_set_format.__qualname__ = class_name
    specialized_set_format.metadata = Metadata(name, description)

    return specialized_set_format
