from enum import Enum, auto
from functools import total_ordering
from typing import Type

from frformat import CustomStrFormat, Metadata
from frformat.common import normalize_value
from frformat.options import Options
from frformat.versioned_set import Version, VersionedSet


@total_ordering
class Millesime(Enum, Version):
    M2023 = auto()
    M2024 = auto()

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def __lt__(self, other) -> bool:
        return self.value < other.value

    def get_id(self) -> str:
        return str(self.value)

    @classmethod
    def is_sorted(cls) -> bool:
        return True


def new(
    class_name: str,
    name: str,
    description: str,
    versionned_geographical_enums: VersionedSet,
) -> Type:
    class GeoEnumFormatVersionned(CustomStrFormat):
        """Checks if a value is in a given geographical referential, with validation for the vintage of choice

        Geographical data in France is revised once a year, with new valid values set given by the "Code Officiel Géographique" (cog).
        """

        def __init__(self, cog: Millesime, options: Options = Options()):
            self._options = options

            _normalized_extra_values = {
                normalize_value(e, self._options)
                for e in self._options.extra_valid_values
            }

            if cog not in versionned_geographical_enums.ls():
                raise ValueError(
                    f"No data available for official geographical code (cog): {cog.name}"
                )

            _valid_values = versionned_geographical_enums.get_data(cog.get_id())
            if _valid_values is not None:
                self._normalized_geo_enum_value = {
                    normalize_value(val, self._options) for val in _valid_values
                }.union(_normalized_extra_values)
            else:
                raise ValueError("There is No valid values! ")

        metadata = Metadata(name, description)

        def is_valid(self, value: str) -> bool:
            normalized_value = normalize_value(value, self._options)
            return normalized_value in self._normalized_geo_enum_value

    GeoEnumFormatVersionned.__name__ = class_name
    GeoEnumFormatVersionned.__qualname__ = class_name

    return GeoEnumFormatVersionned
