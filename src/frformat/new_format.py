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


class BaseFormat(CustomStrFormat):
    def __init__(self, data: Union[FrozenSet, None], options: Options = Options()):
        self._options = options
        self._data = data

        normalized_extra_values = {
            normalize_value(e, self._options) for e in self._options.extra_valid_values
        }

        if self._data is None:
            raise ValueError("There is no data")

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
    def get_geo_data(cog: Union[Millesime, str]) -> Union[FrozenSet, None]:
        if isinstance(valid_data, VersionedSet):
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
        return None

    class GeoFormat(BaseFormat):
        def __init__(self, cog: Union[Millesime, str], options: Options = Options()):
            super().__init__(get_geo_data(cog), options)

            data = get_geo_data(cog)
            if data is None:
                raise ValueError(f"Geographical data for cog '{cog}' is not available.")

            self._normalized_values = {
                normalize_value(val, self._options) for val in data
            }

        metadata = Metadata(name, description)

    def get_enum_data() -> Union[FrozenSet, None]:
        return valid_data if isinstance(valid_data, FrozenSet) else None

    class EnumFormat(BaseFormat):
        def __init__(self, options: Options = Options()):
            super().__init__(get_enum_data(), options)

        metadata = Metadata(name, description)

    if isinstance(valid_data, VersionedSet):
        GeoFormat.__name__ = class_name
        GeoFormat.__qualname__ = class_name
        return GeoFormat
    
    EnumFormat.__name__ = class_name
    EnumFormat.__qualname__ = class_name
    return EnumFormat
