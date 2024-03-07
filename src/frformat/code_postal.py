from frformat.code_postal_set import CODE_POSTAL_SET

from . import CustomFormat


class PostalCode(CustomFormat):
    @classmethod
    def name(cls) -> str:
        return "Code postal"

    @classmethod
    def description(cls) -> str:
        return "Vérifie que le code postal est bien un code postal français"

    @classmethod
    def is_valid(cls, value: str) -> bool:
        return value in CODE_POSTAL_SET

    @classmethod
    def _format(cls, value: str) -> str:
        return value
