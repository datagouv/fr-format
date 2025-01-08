from typing import (
    Dict,
    FrozenSet,
    Generic,
    List,
    Protocol,
    Tuple,
    TypeVar,
    Union,
    cast,
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
        following comparison operators `__lt__()`, `__le__()`, `__gt__()`, `__ge__()`, `__eq__()` and `__ne__()`.
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

    def __ne__(self, v) -> bool:
        ...


class VersionedSet(Generic[V]):
    """
    Allows to store several versions of data and request any of these
    versions.

    Version IDs should be unique.
    """

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

    def get_data(self, version_id: str) -> Union[Data, None]:
        """
        Get the data associated with the given version ID.

        If no data exists for the specified version, the method returns None.

        If the version type is sortable, and there is at least one version, then "latest" is a reserved ID, which returns the data associated
        with the version having the highest id. If the version type is not sortable, or if there is no data, "latest" has no specific meaning.
        """
        version_list = self.ls()

        if len(version_list) != 0:
            version_class = type(version_list[0])

            if version_id == "latest" and version_class.is_sorted():
                if all(isinstance(v, _SortableVersion) for v in version_list):
                    casted_version_list = cast(List[_SortableVersion], version_list)
                    latest_version = max(casted_version_list)
                    _, data = self._versionned_data[latest_version.get_id()]
                    return data

                else:
                    raise AttributeError(
                        "Version class with `is_sorted() == True` should be sortable (see documentation)."
                    )

        data_with_version = self._versionned_data.get(version_id)
        return data_with_version[1] if data_with_version else None
