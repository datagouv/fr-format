from dataclasses import dataclass
from typing import (
    Dict,
    FrozenSet,
    Generic,
    List,
    Protocol,
    Tuple,
    Type,
    TypeVar,
    runtime_checkable,
)

Data = FrozenSet

V = TypeVar("V", bound="Version")


class Version(Protocol):
    def get_id(self) -> str:
        ...

    @classmethod
    def is_sorted(cls) -> bool:
        """If a version class declares itself sorted, it should be sortable by implementing all six
        following comparison operators `__lt__()`, `__le__()`, `__gt__()`, `__ge__()`, `__eq__()` and `__neq__()`.
        See the `functools.total_ordering` decorator helper documentation.
        """
        return False


@runtime_checkable
class _SortableVersion(Version, Protocol):
    """A version subclass that is sortable
    For type checking purposes only"""

    def __lt__(self, v) -> bool:
        ...

    def __le__(self, v) -> bool:
        ...

    def __gt__(self, v) -> bool:
        ...

    def __ge__(self, v) -> bool:
        ...

    def __eq__(self, v) -> bool:
        ...

    def __neq__(self, v) -> bool:
        ...


@dataclass(frozen=True, order=True)
class BaseVersion(Version):
    id: str

    def get_id(self) -> str:
        return self.id


class VersionedSet(Generic[V]):
    """
    Allows to store several versions of data and request any of these
    versions.

    Version IDs should be unique.

    """

    _version_class: Type[V]

    def __init__(self):
        self._versionned_data: Dict[str, Tuple[V, Data]] = {}

    def ls(self) -> List[V]:
        """List all available versions"""
        return [
            self._versionned_data[id][0] for id in sorted(self._versionned_data.keys())
        ]

    def add_version(self, new_version: V, data: Data):
        """Adds a version of data

        Adding a version with already existing ID results in a ValueError.

        """
        if new_version.get_id() in self._versionned_data.keys():
            raise ValueError(f"The version id {new_version.get_id()} already exists!")

        self._versionned_data.update({new_version.get_id(): (new_version, data)})

    def get_data(self, version_id: str) -> Data | None:
        """
        Get the data associated with the given version ID.

        If no data exists for the specified version, the method returns None.

        If the version id is "latest", the method returns the data associated
        with the version having the highest id.
        """

        if self._version_class.is_sorted() and version_id == "latest":
            version_list = self.ls()
            assert (
                version_list is List[_SortableVersion]
            ), "Version class with `is_sorted() == True` shoud be sortable (see documentation)"
            latest_version = max(version_list)
            _, data = self._versionned_data[latest_version.id]
            return data

        data_with_version = self._versionned_data.get(version_id)
        return data_with_version[1] if data_with_version else None
