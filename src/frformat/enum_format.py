from typing import Optional, Set

from frformat import CustomFormat
from frformat.common import normalize_text


def new(
    name: str,
    description: str,
    strict_enum: Set[str],
    lenient_enum: Optional[Set[str]] = None,
):
    if not lenient_enum:
        lenient_enum = {normalize_text(e) for e in strict_enum}

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
                return norm_value in lenient_enum
            else:
                return value in strict_enum

    return EnumFormat
