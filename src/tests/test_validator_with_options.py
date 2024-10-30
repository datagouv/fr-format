from typing import Dict, FrozenSet, List

from frformat import enum_format
from frformat.options import Options


def test_validator():
    _valid_values_enum: FrozenSet[str] = frozenset({"Bonjour", "Réunion"})

    _Validator = enum_format.new(
        "Validator", "validator", "Test validator", _valid_values_enum
    )

    _test_cases: List[Dict[str, Options | List[str]]] = [
        {
            "options": Options(ignore_case=True),
            "valid_cases": ["bonjour"],
            "invalid_cases": ["Bonjour  "],
        },
        {
            "options": Options(ignore_accents=True),
            "valid_cases": ["Reunion"],
            "invalid_cases": ["réunion"],
        },
    ]

    for tc in _test_cases:
        invalid_c = tc["invalid_cases"]
        valid_c = tc["valid_cases"]

        if isinstance(valid_c, List) and isinstance(invalid_c, List):
            for valid_ele in valid_c:
                assert _Validator(tc["options"]).is_valid(
                    valid_ele
                ), f"Check that {valid_ele} is not valid"

            for invalid_ele in invalid_c:
                assert not _Validator(tc["options"]).is_valid(
                    invalid_ele
                ), f"Check that {invalid_ele} is valid"
