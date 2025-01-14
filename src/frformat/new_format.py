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


def _new_enum_format(
    class_name: str,
    name: str,
    description: str,
    valid_data: FrozenSet[str],
) -> Type:
    class EnumFormat(CustomStrFormat):
        metadata = Metadata(name, description)

        def __init__(self, options: Options = Options()):
            self._options = options
            self._data = valid_data

            normalized_extra_values = {
                normalize_value(e, self._options)
                for e in self._options.extra_valid_values
            }

            if self._data is None:
                raise ValueError("There is no data")

            self._normalized_values = {
                normalize_value(e, self._options) for e in self._data
            }.union(normalized_extra_values)

        def is_valid(self, value: str) -> bool:
            normalized_value = normalize_value(value, self._options)
            return normalized_value in self._normalized_values

    EnumFormat.__name__ = class_name
    EnumFormat.__qualname__ = class_name
    return EnumFormat


def new(
    class_name: str,
    name: str,
    description: str,
    valid_data: Union[VersionedSet, FrozenSet[str]],
) -> Type:
    if isinstance(valid_data, VersionedSet):

        def get_geo_data(cog: Union[Millesime, str]) -> FrozenSet:
            try:
                cog = Millesime(cog)
            except ValueError:
                raise ValueError(f"Invalid cog parameter: {cog}")
            cog_data = valid_data.get_data(cog.get_id())
            if cog_data is None:
                raise ValueError(
                    f"No data available for geographical code: {cog.value}"
                )
            return cog_data

        class GeoFormat:
            def __init__(
                self, cog: Union[Millesime, str], options: Options = Options()
            ):
                data = get_geo_data(cog)
                specific_enum_format_cls = _new_enum_format(
                    class_name, name, description, data
                )
                self._enum_format = specific_enum_format_cls(options)

            def is_valid(self, value: str) -> bool:
                return self._enum_format.is_valid(value)

        GeoFormat.__name__ = class_name
        GeoFormat.__qualname__ = class_name
        return GeoFormat

    else:
        return _new_enum_format(class_name, name, description, valid_data)
