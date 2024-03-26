from typing import Set

from frformat import CustomFormat
from frformat.common import normalize_text


def new(name: str, description: str, enum: Set[str]):
    class EnumFormat(CustomFormat):
        """Checks if a value is in a given list

        May check with or without string normalization with the "strict"
        validation.
        """

        @classmethod
        def name(cls) -> str:
            return name

        @classmethod
        def description(cls) -> str:
            return description

        @classmethod
        def is_valid(cls, value: str, strict: bool = True) -> bool:
            if not strict:
                norm_value = normalize_text(value)
                norm_enum = {normalize_text(e) for e in enum}
                return norm_value in norm_enum
            else:
                return value in enum

    return EnumFormat
