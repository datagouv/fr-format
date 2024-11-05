from typing import Dict, FrozenSet, List, Union

from frformat import enum_format
from frformat.options import Options


def test_validator():
    valid_values_enum: FrozenSet[str] = frozenset(
        {"Bonjour", "Réunion", "Plane!", "Fly   ", "La liste"}
    )

    Validator = enum_format.new(
        "Validator", "validator", "Test validator", valid_values_enum
    )

    test_cases: List[Dict[str, Union[Options, List[str]]]] = [
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
        {
            "options": Options(replace_non_alphanumeric_with_space=True),
            "valid_cases": ["Plane!", "Plane "],
            "invalid_cases": [" Plane! "],
        },
        {
            "options": Options(ignore_extra_whitespace=True),
            "valid_cases": [" Fly   "],
            "invalid_cases": ["fly  "],
        },
        {
            "options": Options(
                ignore_case=True, extra_valid_values=frozenset({"Hello"})
            ),
            "valid_cases": ["hello", "Réunion"],
            "invalid_cases": ["Hello!!", " réunion"],
        },
        {
            "options": Options(
                ignore_accents=True,
                replace_non_alphanumeric_with_space=True,
                ignore_extra_whitespace=True,
                extra_valid_values=frozenset({"#  paramétre "}),
            ),
            "valid_cases": ["paramétre", "parametre", "Plane"],
            "invalid_cases": ["plane", "#  Paramétre "],
        },
        {
            "options": Options(
                ignore_case=True,
                ignore_accents=True,
                replace_non_alphanumeric_with_space=True,
                ignore_extra_whitespace=True,
                extra_valid_values=frozenset({"Coordonnées"}),
            ),
            "valid_cases": ["coordonnées", "coordonnees", "la  liste ", "La$$liste"],
            "invalid_cases": ["Coord onnées"],
        },
        {
            "options": Options(
                ignore_case=True,
                replace_non_alphanumeric_with_space=True,
                ignore_extra_whitespace=True,
            ),
            "valid_cases": [" la  liste  ", "bonjour!"],
            "invalid_cases": ["Bon jour", "reunion "],
        },
    ]

    for tc in test_cases:
        invalid_c = tc["invalid_cases"]
        valid_c = tc["valid_cases"]

        if isinstance(valid_c, List) and isinstance(invalid_c, List):
            for valid_ele in valid_c:
                assert Validator(tc["options"]).is_valid(
                    valid_ele
                ), f"Check that {valid_ele} is not valid"

            for invalid_ele in invalid_c:
                assert not Validator(tc["options"]).is_valid(
                    invalid_ele
                ), f"Check that {invalid_ele} is valid"
