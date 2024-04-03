from typing import List, TypedDict

from frformat import Region
from tests.testing import validation_test_helper_factory

aux_test_region = validation_test_helper_factory(Region)


def test_region():
    TestCase = TypedDict(
        "TestCase",
        {"values": List[str], "isStrictValidation": bool, "expectValid": bool},
    )

    test_cases: List[TestCase] = [
        {
            "values": ["Centre-Val de Loire", "La Réunion", "Corse"],
            "isStrictValidation": True,
            "expectValid": True,
        },
        {
            "values": ["Centre Val de Loire", "La Reunion", "corse"],
            "isStrictValidation": True,
            "expectValid": False,
        },
        {
            "values": [
                "Centre-Val de Loire",
                "La Réunion",
                "Corse",
                "Centre Val de Loire",
                "La Reunion",
                "corse",
                "bfc",
                "aura",
            ],
            "isStrictValidation": False,
            "expectValid": True,
        },
        {
            "values": ["Haute-Vienne", "Val-de-Marne"],
            "isStrictValidation": False,
            "expectValid": False,
        },
    ]

    for tc in test_cases:
        aux_test_region(tc["values"], tc["isStrictValidation"], tc["expectValid"])
