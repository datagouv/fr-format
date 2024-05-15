import re

from frformat import CustomStrFormat

name = "Code RNA"
description = "Vérifie les codes RNA (Répertoire National des Associations) valides"


class CodeRNA(CustomStrFormat):
    @classmethod
    def name(cls) -> str:
        return name

    @classmethod
    def description(cls) -> str:
        return description

    @classmethod
    def is_valid(cls, value: str) -> bool:
        return bool(re.match(r"^W\d{9}$", value))

    @classmethod
    def _format(cls, value: str) -> str:
        return f"{value[0:4]}\u00A0{value[4:7]}\u00A0{value[7:]}"
