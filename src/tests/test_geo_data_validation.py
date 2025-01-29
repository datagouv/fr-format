import pytest

from frformat.set_format import Millesime, new
from frformat.versioned_set import VersionedSet


def test_geo_data_format():
    versioned_data = VersionedSet[Millesime]()
    versioned_data.add_version(
        Millesime.M2023,
        frozenset({"Ambléon", "Ambronay"}),
    )

    versioned_data.add_version(Millesime.M2024, frozenset({"Arandas"}))

    FormatTest = new(
        "Versionned format", "Versionned format", "Versionned format", versioned_data
    )

    test_cases = [
        {
            "version": Millesime.M2023,
            "value_to_test": "Ambléon",
            "expected_valid": True,
        },
        {
            "version": Millesime.M2023,
            "value_to_test": "Anglefort",
            "expected_valid": False,
        },
        {
            "version": Millesime.M2024,
            "value_to_test": "Arandas",
            "expected_valid": True,
        },
        {
            "version": Millesime.LATEST,
            "value_to_test": "Arandas",
            "expected_valid": True,
        },
        {
            "version": Millesime.LATEST,
            "value_to_test": "Ambléon",
            "expected_valid": False,
        },
        {"version": "2025", "expected_error": ValueError},
    ]

    for tc in test_cases:
        if "expected_error" in tc:
            with pytest.raises(tc["expected_error"]):
                FormatTest(tc["version"])
        else:
            test_format = FormatTest(tc["version"])
            assert (
                test_format.is_valid(tc["value_to_test"]) == tc["expected_valid"]
            ), f'Error on geo data format definition with version { tc["version"] } and value { tc["value_to_test"] }'
