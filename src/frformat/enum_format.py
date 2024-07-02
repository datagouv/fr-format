from typing import Set, Type

from frformat import CustomStrFormat, Metadata
from frformat.common import normalize_value
from frformat.options import Options


def new(class_name: str, name: str, description: str, enum: Set[str]) -> Type:
    class EnumFormat(CustomStrFormat):
        """Checks if a value is in a given list

        May check with string normalization with the "options" of validation."""

        metadata = Metadata(name, description)

        @classmethod
        def is_valid(cls, value: str, options: Options = Options()) -> bool:
            normalized_enum = {normalize_value(e, options) for e in enum}
            normalized_value = normalize_value(value, options)

            return normalized_value in normalized_enum

    EnumFormat.__name__ = class_name
    EnumFormat.__qualname__ = class_name

    return EnumFormat
