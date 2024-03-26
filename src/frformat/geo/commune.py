from frformat import CustomFormat
from frformat.common import normalize_text
from frformat.geo.commune_set import COMMUNE_SET


class Commune(CustomFormat):
    @classmethod
    def name(cls) -> str:
        return "Nom de commune"

    @classmethod
    def description(cls) -> str:
        return (
            "Vérifie que le nom correspond à un nom de commune française "
            "(ne vérifie pas l'accentuation, la casse, la ponctuation)"
        )

    @classmethod
    def is_valid(cls, value: str) -> bool:
        normalized_value = normalize_text(value)
        return normalized_value in COMMUNE_SET
