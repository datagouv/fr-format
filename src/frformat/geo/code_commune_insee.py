from frformat import CustomFormat
from frformat.geo.code_commune_insee_set import CODE_COMMUNE_INSEE_SET


class CodeCommuneInsee(CustomFormat):
    @classmethod
    def name(cls) -> str:
        return "Code commune INSEE"

    @classmethod
    def description(cls) -> str:
        return "Vérifie que le code commune correspond bien à un code commune INSEE"

    @classmethod
    def is_valid(cls, value: str) -> bool:
        return value in CODE_COMMUNE_INSEE_SET
