from frformat import CustomFormat
from frformat.common import normalize_text
from frformat.geo.departement_set import DEPARTEMENT_SET


class Departement(CustomFormat):
    @classmethod
    def name(cls) -> str:
        return "Nom de département"

    @classmethod
    def description(cls) -> str:
        return (
            "Vérifie les départements français valides (code officiel géographique 2020) "
            "(ne vérifie pas l'accentuation, la casse, la ponctuation)"
        )

    @classmethod
    def is_valid(cls, value: str) -> bool:
        normalized_value = normalize_text(value)
        return normalized_value in DEPARTEMENT_SET
