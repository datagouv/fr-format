from typing import Set

from frformat import CustomStrFormat

name = "Code RNA"
description = "Vérifie les codes RNA valides"


class CodeRNA(CustomStrFormat):
    @classmethod
    def name(cls) -> str:
        return name

    @classmethod
    def description(cls) -> str:
        return description

    @classmethod
    def is_valid(cls, value: str) -> bool:
        digits: Set[str] = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        if len(value) != 10:
            return False

        if value[0] != "w" and value[0] != "W":
            return False

        boolResult: bool = True
        index: int = 1
        while index <= len(value) - 1:
            if not value[index] in digits:
                boolResult = False
                break
            index = index + 1

        return boolResult
