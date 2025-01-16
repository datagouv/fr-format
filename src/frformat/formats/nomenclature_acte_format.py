from typing import List, Literal, Tuple, Union

from frformat import CustomStrFormat, Metadata
from frformat.common import normalize_value
from frformat.options import Options

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

    def __init__(
        self, options: Options = Options(ignore_accents=True, ignore_case=True)
    ):
        """Initializes the `NomenclatureActe` class with customizable validation options.
        By default, the validation is case-insensitive and accent-insensitive, ensuring that values and authorized_values are normalized
        accordingly before comparison.
        """
        self._options = options
        self._normalized_autho_values = {
            normalize_value(ae, self._options) for ae in AUTHORIZED_VALUES
        }

    def is_valid(
        self,
        value: str,
    ) -> bool:
        nomenc = self._nomenclature(value)
        normalized_nomenc = normalize_value(nomenc, self._options)

        # Nomenclature reconnue et pas d'espace après l'oblique
        return "/ " not in value and normalized_nomenc in self._normalized_autho_values

    def is_valid_with_details(
        self, value: str
    ) -> Union[ValidWithoutDetails, InvalidWithDetails]:
        """Check the validity, and return details if value is invalid"""

        details = []
        if self.is_valid(value):
            return (True, None)

        if "/" not in value:
            details.append(MISSING_SLASH)

        else:
            nomenc = self._nomenclature(value)

            if nomenc.rstrip() in AUTHORIZED_VALUES or "/ " in value:
                details.append(EXTRA_SPACE)

            if nomenc.strip() not in AUTHORIZED_VALUES:
                details.append(INVALID_PREFIX(nomenc.strip()))

        return (False, details)

    @staticmethod
    def _nomenclature(value: str) -> str:
        return value[: value.find("/")]
