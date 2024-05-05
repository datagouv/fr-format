import re

from frformat import CustomStrFormat

name = "Code RNA"
description = "Vérifie les codes RNA valides"


class CodeRna(CustomStrFormat):
    @classmethod
    def name(cls) -> str:
        return name

    @classmethod
    def description(cls) -> str:
        return description

    @classmethod
    def is_valid(cls, value: str) -> bool:
        """Repere le code RNA"""
        return bool(re.match(r"^[wW]\d{9}$", value))
