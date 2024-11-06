from typing import FrozenSet, Type

from frformat import CustomStrFormat, Metadata
from frformat.common import normalize_value
from frformat.options import Options


def new(class_name: str, name: str, description: str, enum: FrozenSet[str]) -> Type:
    class EnumFormat(CustomStrFormat):
        """Checks if a value is in a given list

        May preprocess the input and valid values according to given "options"."""

        def __init__(self, options: Options = Options()):
            self._options = options

            _normalized_extra_values = {
                normalize_value(e, self._options)
                for e in self._options.extra_valid_values
            }

            self._normalized_enum = {
                normalize_value(e, self._options) for e in enum
            }.union(_normalized_extra_values)

        metadata = Metadata(name, description)

        def is_valid(self, value: str) -> bool:
            normalized_value = normalize_value(value, self._options)
            return normalized_value in self._normalized_enum

    EnumFormat.__name__ = class_name
    EnumFormat.__qualname__ = class_name

    return EnumFormat
