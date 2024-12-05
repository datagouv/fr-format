from dataclasses import dataclass
from typing import Dict, FrozenSet, List

Data = FrozenSet


@dataclass(frozen=True, order=True)
class Version:
    id: str

    # Functions to be sorted, with default sorting by id


class VersionedSet:
    """
    Allows to store several versions of data and request any of these
    versions.

    version = "latest" ? What behavior ?
    """

    def __init__(self):
        self._version: Dict[Version, Data] = {}

    def ls(self) -> List[Version]:
        """List all available versions"""
        return sorted(self._version.keys())

    def add_version(self, new_version: Version, data: Data):
        if new_version in self._version.keys():
            raise ValueError(f"The version id {new_version.id} already exists!")

        self._version.update({new_version: data})

    def get_data(self, version: Version) -> Data | None:
        """
        Get the data associated with the given version.

        If the version id is "latest", the method returns the data associated
        with the version having the highest id. If no data exists for the
        specified version, or if the VersionedSet is empty, the method returns None.

        """
        if len(self._version) == 0:
            return None

        if version.id == "latest":
            latest_version = max(self._version.keys())
            return self._version[latest_version]

        return self._version.get(version)


vs = VersionedSet()
vs.add_version(Version("2025"), frozenset({"coucou"}))  # ok
vs.add_version(Version("2024"), frozenset({"one"}))  # ok
vs.add_version(Version("2024"), frozenset({"two"}))  # not ok

print(vs.ls())

vs_getted = vs.get_data(Version("2005"))  # ok
print("returned data: ", vs_getted)
vs.get_data(Version("204"))  # not ok


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
