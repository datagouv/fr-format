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

    def add_version(self, version_id: str, data: Data):
        if not version_id.isnumeric():
            raise ValueError(f"Version id {version_id} should be numeric")

        new_version = Version(version_id)

        if new_version in self._version.keys():
            raise ValueError(f"The version id {version_id} already exists!")

        self._version.update({new_version: data})

    # get_data_version ??
    def get_version(self, version_id: str) -> Data:
        if (self._version.get(Version(version_id))) is not None:
            data = self._version[Version(version_id)]
        else:
            print("This version_id doesn't exist !")
            data = frozenset({})

        return data


vs = VersionedSet()
vs.add_version("2025", frozenset({"coucou"}))  # ok
vs.add_version("2024", frozenset({"one"}))  # ok
# vs.add_version("2024", frozenset({"two"}))  # not ok
# vs.add_version("string", frozenset({"Hi"}))  # not ok

print(vs.ls())

"""vs_getted = vs.get_version("2025")  # ok
print("returned data: ", vs_getted)
vs.get_version("204")  # not ok
 """

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
