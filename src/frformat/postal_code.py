from frformat.postal_code_set import POSTAL_CODE_SET

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
        return value in POSTAL_CODE_SET

    @classmethod
    def _format(cls, value: str) -> str:
        return value
