from typing import FrozenSet

Data = FrozenSet


class VersionedSet:
    """
    Allows to store several versions of data and request any of these
    versions.

    version = "latest" ? What behavior ?
    """

    def ls():
        """List all available versions"""
        pass

    def add_version(self, version_id: Version, data: Data):
        pass

    def get_version(self, version_id: Version) -> Data:
        pass


@dataclass
class Version:
    self.id: str

    # Functions to be sorted, with default sorting by id


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
