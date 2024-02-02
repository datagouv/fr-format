import unicodedata
from typing import List, Literal, Tuple, Union

from . import CustomFormat

AUTHORIZED_VALUES = set(
    [
        "Commande publique",
        "Urbanisme",
        "Domaine et patrimoine",
        "Fonction publique",
        "Institutions et vie politique",
        "Libertés publiques et pouvoirs de police",
        "Finances locales",
        "Domaines de compétences par thèmes",
        "Autres domaines de compétences",
    ]
)

MISSING_SLASH = "le signe oblique « / » est manquant"

EXTRA_SPACE = "le signe oblique ne doit pas être précédé ni suivi d'espace"


def INVALID_PREFIX(prefix: str) -> str:
    return f"le préfixe de nomenclature Actes {prefix!r} n'est pas reconnu"


class NomenclatureActe(CustomFormat):
    @classmethod
    def name(cls) -> str:
        return "Nomenclature des actes"

    @classmethod
    def description(cls) -> str:
        return """
        Document de référence dans les spécifications SCDL :
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

    @classmethod
    def is_valid(cls, value: str) -> bool:
        nomenc = value[: value.find("/")]
        nomenclatures = AUTHORIZED_VALUES

        # Nomenclature reconnue et pas d'espace avant ni après l'oblique
        if "/ " not in value and nomenc in nomenclatures:
            return True
        else:
            return False

    @classmethod
    def is_valid_with_details(
        cls, value: str
    ) -> Union[Tuple[Literal[True], None], Tuple[Literal[False], List[str]]]:
        """Check the validity, and return details if value is invalid"""
        nomenc = value[: value.find("/")]
        nomenclatures = AUTHORIZED_VALUES

        details = []

        if cls.is_valid(value):
            return (True, None)
        if "/" not in value:
            details.append(MISSING_SLASH)
        else:
            if nomenc.rstrip() in nomenclatures or "/ " in value:
                details.append(EXTRA_SPACE)
            if nomenc.strip() not in nomenclatures:
                details.append(INVALID_PREFIX(nomenc.strip()))
        return (False, details)

    @classmethod
    def _format(cls, value: str) -> str:
        return value


# def norm_str(s):
#     """Normalize string, i.e. removing accents and turning into lowercases"""
#     return "".join(
#         c
#         for c in unicodedata.normalize("NFD", s.lower())
#         if unicodedata.category(c) != "Mn"
#     )
