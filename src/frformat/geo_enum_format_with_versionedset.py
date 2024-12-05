from typing import Type

from frformat import CustomStrFormat, Metadata
from frformat.common import normalize_value
from frformat.options import Options
from frformat.utils.versioned_set import Version, VersionedSet


def new(
    class_name: str,
    name: str,
    description: str,
    geographical_enums: VersionedSet,
) -> Type:
    class GeoEnumFormat(CustomStrFormat):
        """Checks if a value is in a given geographical referential, with validation for the vintage of choice

        Geographical data in France is revised once a year, with new valid values set given by the "Code Officiel Géographique" (cog).
        """

        def __init__(self, version: Version, options: Options = Options()):
            self._options = options

            _normalized_extra_values = {
                normalize_value(e, self._options)
                for e in self._options.extra_valid_values
            }

            if not version.id.isnumeric():
                lower_version_id = version.id.lower()

                if lower_version_id == "latest":
                    _valid_values = geographical_enums.get_data(version.id)

                    if _valid_values is None:
                        raise ValueError("No available data for the latest version!")
                else:
                    raise ValueError(f"Invalid version id {version.id}")
            else:
                _valid_values = geographical_enums.get_data(version.id)
                if _valid_values is None:
                    raise ValueError(f"No available data this version {version.id}!")

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
