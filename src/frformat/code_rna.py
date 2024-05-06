from typing import List

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
        first_letter: List[str] = ["w", "W"]
        digits: List[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        if len(value) < 10 or not value[9] in digits or not value[0] in first_letter:
            return False

        boolResult: bool = True
        index: int = 1
        while index <= len(value) - 1:
            if not value[index] in digits:
                boolResult = False
                break
            index = index + 1

        return boolResult
