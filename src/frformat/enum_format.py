from enum import Enum
from typing import Dict, Set, Type

from frformat import CustomStrFormat, Metadata
from frformat.common import normalize_value
from frformat.options import Options


def new(
    class_name: str, name: str, description: str, geographical_enum: Dict[str, Set[str]]
) -> Type:
    class GeographicalEnum(Enum):
        COG_2023 = 2023
        COG_2024 = 2024

    class EnumFormat(CustomStrFormat):
        """Checks if a value is in a given list

        May preprocess the input and valid values according to given "options" and the "Official Geographic Code"
        """

        def __init__(self, cog: GeographicalEnum, options: Options = Options()):
            self._options = options

            _normalized_extra_values = {
                normalize_value(e, self._options)
                for e in self._options.extra_valid_values
            }

            if cog.name not in geographical_enum.keys():
                raise ValueError(f"Invalid geographical enum: {cog.name}")

            self._normalized_geo_enum_value = {
                normalize_value(code, self._options)
                for value in geographical_enum.values()
                for code in value
            }.union(_normalized_extra_values)

        metadata = Metadata(name, description)

        def is_valid(self, value: str) -> bool:
            normalized_value = normalize_value(value, self._options)
            return normalized_value in self._normalized_geo_enum_value

    EnumFormat.__name__ = class_name
    EnumFormat.__qualname__ = class_name

    return EnumFormat
