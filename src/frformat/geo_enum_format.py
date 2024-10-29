from enum import Enum, auto
from typing import Dict, FrozenSet, Type

from frformat import CustomStrFormat, Metadata
from frformat.common import normalize_value
from frformat.options import Options


class Millesime(Enum):
    A2023 = auto()
    A2024 = auto()


def new(
    class_name: str,
    name: str,
    description: str,
    geographical_enums: Dict[Millesime, FrozenSet[str]],
) -> Type:
    class GeoEnumFormat(CustomStrFormat):
        """Checks if a value is in a given geographical referential, with validation for the vintage of choice

        Geographical data in France is revised once a year, with new valid values set given by the "Code Officiel Géographique" (cog).
        """

        def __init__(self, cog: Millesime, options: Options = Options()):
            self._options = options

            _normalized_extra_values = {
                normalize_value(e, self._options)
                for e in self._options.extra_valid_values
            }

            if cog not in geographical_enums.keys():
                raise ValueError(
                    f"No data available for official geographical code (cog): {cog.name}"
                )

            _valid_values = geographical_enums[cog]

            self._normalized_geo_enum_value = {
                normalize_value(val, self._options) for val in _valid_values
            }.union(_normalized_extra_values)

        metadata = Metadata(name, description)

        def is_valid(self, value: str) -> bool:
            normalized_value = normalize_value(value, self._options)
            return normalized_value in self._normalized_geo_enum_value

    GeoEnumFormat.__name__ = class_name
    GeoEnumFormat.__qualname__ = class_name

    return GeoEnumFormat
