from typing import List, Literal, Tuple, Union

from . import CustomFormat

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

        # Nomenclature reconnue et pas d'espace avant ni après l'oblique
        if "/ " not in value and nomenc in AUTHORIZED_VALUES:
            return True
        else:
            return False

    @classmethod
    def is_valid_with_details(
        cls, value: str
    ) -> Union[ValidWithoutDetails, InvalidWithDetails]:
        """Check the validity, and return details if value is invalid"""
        nomenc = value[: value.find("/")]

        details = []

        if cls.is_valid(value):
            return (True, None)

        if "/" not in value:
            details.append(MISSING_SLASH)

        else:
            if nomenc.rstrip() in AUTHORIZED_VALUES or "/ " in value:
                details.append(EXTRA_SPACE)

            if nomenc.strip() not in AUTHORIZED_VALUES:
                details.append(INVALID_PREFIX(nomenc.strip()))

        return (False, details)

    @classmethod
    def _format(cls, value: str) -> str:
        return value
