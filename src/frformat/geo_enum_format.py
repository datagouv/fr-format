from enum import Enum
from functools import total_ordering
from typing import Type, Union

from frformat import CustomStrFormat, Metadata
from frformat.common import normalize_value
from frformat.options import Options
from frformat.versioned_set import VersionedSet


@total_ordering
class Millesime(Enum):
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


def new(
    class_name: str,
    name: str,
    description: str,
    versionned_geographical_enums: VersionedSet,
) -> Type:
    class GeoEnumFormat(CustomStrFormat):
        """Checks if a value is in a given geographical referential, with validation for the vintage of choice

        Geographical data in France is revised once a year, with new valid values set given by the "Code Officiel Géographique" (cog).
        """

        def __init__(self, cog: Union[Millesime, str], options: Options = Options()):
            self._options = options
            
            try:
                self._cog = Millesime(cog)
            except ValueError:
                raise ValueError(f"cog parameter {cog} is invalid ")

            _normalized_extra_values = {
                normalize_value(e, self._options)
                for e in self._options.extra_valid_values
            }

            if self._cog not in versionned_geographical_enums.ls():
                raise ValueError(
                    f"No data available for official geographical code (cog): {self._cog.value}"
                )

            _valid_values = versionned_geographical_enums.get_data(self._cog.get_id())

            if _valid_values is not None:
                self._normalized_geo_enum_value = {
                    normalize_value(val, self._options) for val in _valid_values
                }.union(_normalized_extra_values)
            else:
                raise ValueError("There is no data associated to this cog {} ")

        metadata = Metadata(name, description)

        def is_valid(self, value: str) -> bool:
            normalized_value = normalize_value(value, self._options)
            return normalized_value in self._normalized_geo_enum_value

    GeoEnumFormat.__name__ = class_name
    GeoEnumFormat.__qualname__ = class_name

    return GeoEnumFormat
