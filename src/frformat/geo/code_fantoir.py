import string

from frformat import CustomFormat
from frformat.geo.code_fantoir_set import PARTIAL_CODE_FANTOIR_SET

name = "Code fantoir"
description = "Vérifie les codes fantoirs valides"

UPPER_LETTERS = string.ascii_uppercase


class CodeFantoir(CustomFormat):
    @classmethod
    def name(cls) -> str:
        return name

    @classmethod
    def description(cls) -> str:
        return description

    @classmethod
    def is_valid(cls, value: str) -> bool:
        if len(value) != 5:
            return False

        return value[4] in UPPER_LETTERS and value[:4] in PARTIAL_CODE_FANTOIR_SET

    @classmethod
    def _format(cls, value: str) -> str:
        return f"{value[0:3]} {value[3:6]} {value[6:]}"
