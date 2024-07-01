from typing import Optional, Set, Type

from frformat import CustomStrFormat, Metadata
from frformat.common import normalize_text
from frformat.options import Options


def new(
    class_name: str,
    name: str,
    description: str,
    strict_enum: Set[str],
    lenient_enum: Optional[Set[str]] = None,
) -> Type:
    if not lenient_enum:
        options = Options(
            ignore_case=True,
            ignore_punctuation=True,
            ignore_underscore=True,
            ignore_fullwidth_apostrophe=True,
            ignore_space=True,
            ignore_accents=True,
        )
        lenient_enum = {normalize_text(e, options) for e in strict_enum}

    class EnumFormat(CustomStrFormat):
        """Checks if a value is in a given list

        May check with or without string normalization with the "strict"
        validation.
        """

        metadata = Metadata(name, description)

        @classmethod
        def is_valid(cls, value: str, option_items: Optional[Options] = None) -> bool:
            if option_items is not None:
                norm_value = normalize_text(value, option_items)
                return norm_value in lenient_enum
            else:
                return value in strict_enum

    EnumFormat.__name__ = class_name
    EnumFormat.__qualname__ = class_name

    return EnumFormat
