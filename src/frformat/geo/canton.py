from frformat import CustomFormat
from frformat.common import normalize_text
from frformat.geo.canton_set import CANTON_SET


class Canton(CustomFormat):
    @classmethod
    def name(cls) -> str:
        return "Nom de canton"

    @classmethod
    def description(cls) -> str:
        return (
            "Vérifie les cantons françaises valides (code officiel géographique 2020) "
            "(ne vérifie pas l'accentuation, la casse, la ponctuation)"
        )

    @classmethod
    def is_valid(cls, value: str) -> bool:
        normalized_value = normalize_text(value)
        return normalized_value in CANTON_SET
