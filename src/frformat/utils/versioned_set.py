from dataclasses import dataclass
from typing import Dict, FrozenSet, Generic, List, TypeVar, Tuple

Data = FrozenSet

V = TypeVar("V", bound="Version")


@dataclass(frozen=True, order=True)
class Version:
    id: str

    # Functions to be sorted, with default sorting by id


class VersionedSet(Generic[V]):
    """
    Allows to store several versions of data and request any of these
    versions.

    Version IDs should be unique.

    version = "latest" ? What behavior ?
    """

    def __init__(self):
        self._version: Dict[str, Tuple[V, Data]] = {}

    def ls(self) -> List[V]:
        """List all available versions"""
        return sorted(version for version, _ in self._version.values())

    def add_version(self, new_version: V, data: Data):
        """ Adds a version of data

        Adding a version with already existing ID results in a ValueError.

        """
        if new_version.id in self._version.keys():
            raise ValueError(f"The version id {new_version.id} already exists!")

        self._version.update({new_version.id: (new_version, data)})

    def get_data(self, version_id: str) -> Data | None:
        """
        Get the data associated with the given version ID.

        If no data exists for the specified version, the method returns None.

        If the version id is "latest", the method returns the data associated
        with the version having the highest id.
        """

        if version_id == "latest":
            latest_version = max(self.ls())
            _, data = self._version[latest_version.id]
            return data
        
        version_data = self._version.get(version_id)
        return version_data[1] if version_data else None


vs = VersionedSet()
vs.add_version(Version("2025"), frozenset({"coucou"}))  # ok
vs.add_version(Version("2024"), frozenset({"one"}))  # ok
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
