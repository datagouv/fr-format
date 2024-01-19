import unicodedata
from typing import Literal, Tuple, Union

from . import CustomFormat

AUTHORIZED_VALUES = [
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
        nomenclatures = set(map(norm_str, AUTHORIZED_VALUES))

        # Nomenclature reconnue et pas d'espace avant ni après l'oblique
        if "/ " not in value and norm_str(nomenc) in nomenclatures:
            return True
        else:
            return False

    @classmethod
    def is_valid_with_details(
        cls, value: str
    ) -> Union[Tuple[Literal[True], None], Tuple[Literal[False], str]]:
        """Check the validity, and return details if value is invalid"""
        nomenc = value[: value.find("/")]
        nomenclatures = set(map(norm_str, AUTHORIZED_VALUES))

        if cls.is_valid(value):
            return (True, None)
        elif "/" not in value:
            note = "le signe oblique « / » est manquant"
        elif norm_str(nomenc.rstrip()) in nomenclatures or "/ " in value:
            note = "le signe oblique ne doit pas être précédé ni suivi d'espace"
        else:
            note = f"le préfixe de nomenclature Actes {nomenc!r} n'est pas reconnu"
        return (False, note)

    @classmethod
    def _format(cls, value: str) -> str:
        return value


def norm_str(s):
    """Normalize string, i.e. removing accents and turning into lowercases"""
    return "".join(
        c
        for c in unicodedata.normalize("NFD", s.lower())
        if unicodedata.category(c) != "Mn"
    )
