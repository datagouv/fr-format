from typing import List, Literal, Tuple, Union

from frformat import CustomStrFormat, Metadata
from frformat.common import Options

AUTHORIZED_VALUES = {
    "Commande publique",
    "Urbanisme",
    "Domaine et patrimoine",
    "Fonction publique",
    "Institutions et vie politique",
    "Libertés publiques et pouvoirs de police",
    "Finances locales",
    "Domaines de compétences par thèmes",
    "Autres domaines de compétences",
}

MISSING_SLASH = "le signe oblique « / » est manquant"

EXTRA_SPACE = "le signe oblique ne doit pas être précédé ni suivi d'espace"


def INVALID_PREFIX(prefix: str) -> str:
    return f"le préfixe de nomenclature Actes {prefix!r} n'est pas reconnu"


ValidWithoutDetails = Tuple[Literal[True], None]
InvalidWithDetails = Tuple[Literal[False], List[str]]


name = "Nomenclature des actes"

description = """Document de référence dans les spécifications SCDL :
        http://www.moselle.gouv.fr/content/download/1107/7994/file/nomenclature.pdf

        Dans la nomenclature Actes, les valeurs avant le '/' sont :

        Commande publique
        Urbanisme
        Domaine et patrimoine
        Fonction publique
        Institutions et vie politique
        Libertés publiques et pouvoirs de police
        Finances locales
        Domaines de compétences par thèmes
        Autres domaines de compétences

        La validation devra accepter minuscules et majuscules, accents et sans accents ...
"""


class NomenclatureActe(CustomStrFormat):
    metadata = Metadata(name, description)

    def is_valid(self, value: str) -> bool:
        nomenc = self._nomenclature(value)

        # Nomenclature reconnue et pas d'espace après l'oblique
        return "/ " not in value and nomenc in AUTHORIZED_VALUES

    @classmethod
    def is_valid_with_details(
        cls, value: str
    ) -> Union[ValidWithoutDetails, InvalidWithDetails]:
        """Check the validity, and return details if value is invalid"""

        details = []
        instance = cls(Options())
        if instance.is_valid(value):
            return (True, None)

        if "/" not in value:
            details.append(MISSING_SLASH)

        else:
            nomenc = cls._nomenclature(value)

            if nomenc.rstrip() in AUTHORIZED_VALUES or "/ " in value:
                details.append(EXTRA_SPACE)

            if nomenc.strip() not in AUTHORIZED_VALUES:
                details.append(INVALID_PREFIX(nomenc.strip()))

        return (False, details)

    @staticmethod
    def _nomenclature(value: str) -> str:
        return value[: value.find("/")]
