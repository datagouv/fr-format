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

    version = "latest" ? What behavior ?
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


vs = VersionedSet[BaseVersion]()
vs.add_version(BaseVersion("2025"), frozenset({"coucou"}))  # ok
vs.add_version(BaseVersion("2024"), frozenset({"one"}))  # ok
# vs.add_version(Version("2024"), frozenset({"two"}))  # not ok

print(vs.ls())

vs_getted = vs.get_data("2025")  # ok
print("returned data: ", vs_getted)
vs.get_data("204")  # not ok


"""
OPEN
J'ai un Versionned set, comment je sais quelle 'version_id' je peux utiliser
// leur format

VERSION_ID == STRING ??

Le problème de version_id = str, c'est que en tant qu'utilisateur d'un
VersionedSet, soit j'ai la charge mentale des versions autorisées, soit je
suis obligé de regarde l'implémentation (et le but de l'abstraction c'est
d'éviter ça)

On a plusieurs jeux de données qui ont les mêmes ID de version et la chaîne de
caractère ne permet pas de la garantir.

Et en même temps, on peut imaginer des disponibilités partielles pour les
mêmes ID de version (par exemple: certaines données sont dispos pour des COG
depuis 1990, d'autres seulement depuis 2000)

VERSION_ID == ENUM ??

- Est-ce que c'est simple / intuitif de restreindre un enum à seulement
modalités ?
    - Si oui, ça demande de changer le type à chaque fois qu'on modifie les
      données -> c'est un peu nul
    - Si non -> dans ce cas il faut gérer la situation ou les données ne sont
      pas disponibles. Est-ce que c'est grave :
        - un peu parce que ça donne l'illusion que les données sont
          disponibles
        - le typage n'intercepte pas statiquement une erreur

DONE

Should Data be a Set -> Frozenset

Est-ce que c'est dans le périmètre de cette classe de gérer LATEST ?

"""
