from enum import Enum, auto
from typing import Dict, Set, Type

from frformat import CustomStrFormat, Metadata
from frformat.common import normalize_value
from frformat.options import Options


class Millesime(Enum):
    Y2023 = auto()
    Y2024 = auto()


def new(
    class_name: str,
    name: str,
    description: str,
    geographical_enums: Dict[str, Set[str]],
) -> Type:
    class EnumFormat(CustomStrFormat):
        """Checks if a value is in a given list

        May preprocess the input and valid values according to given "options" and the "Official Geographic Code"
        """

        def __init__(self, cog: Millesime, options: Options = Options()):
            self._options = options

            _normalized_extra_values = {
                normalize_value(e, self._options)
                for e in self._options.extra_valid_values
            }

            if cog.name not in geographical_enums.keys():
                raise ValueError(f"Invalid given cog: {cog.name}")

            _code_set = geographical_enums[cog.name]

            self._normalized_geo_enum_value = {
                normalize_value(code, self._options) for code in _code_set
            }.union(_normalized_extra_values)

        metadata = Metadata(name, description)

        def is_valid(self, value: str) -> bool:
            normalized_value = normalize_value(value, self._options)
            return normalized_value in self._normalized_geo_enum_value

    EnumFormat.__name__ = class_name
    EnumFormat.__qualname__ = class_name

    return EnumFormat
