import pytest

from frformat import set_format
from frformat.set_format import Millesime, new
from frformat.versioned_set import VersionedSet


def test_format_validation():
    versioned_data = VersionedSet[Millesime]()
    versioned_data.add_version(
        Millesime.M2023,
        frozenset({"Ambléon", "Ambronay"}),
    )

    versioned_data.add_version(Millesime.M2024, frozenset({"Arandas"}))

    FormatTest = new(
        "Versionned format",
        "Versionned format name",
        "Versionned format description",
        "Versionned format source",
        versioned_data,
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
            ), f'Error on data format definition with version { tc["version"] } and value { tc["value_to_test"] }'


def test_formats_valid_values():
    versioned_data = VersionedSet[Millesime]()
    versioned_data.add_version(Millesime.M2024, frozenset({"Paris", "Lyon"}))
    test_cases = [
        {
            "name": "VersionedSetFormat",
            "valid_data": versioned_data,
            "version": "2024",
            "expected_result": frozenset({"Paris", "Lyon"}),
        },
        {
            "name": "SingleSetFormat",
            "valid_data": frozenset({"Nomandie", "Nice"}),
            "version": None,
            "expected_result": frozenset({"Nomandie", "Nice"}),
        },
    ]

    name = "Validator name"
    description = "Validator description"
    source = "Validator source"

    for tc in test_cases:
        validator = set_format.new(
            "Validator", name, description, source, tc["valid_data"]
        )
        if tc["version"]:
            assert (
                validator(tc["version"]).get_valid_values_set() == tc["expected_result"]
            ), f"While we test {tc['name']}, the returned data is not equal to {tc['expected_result']} when the valid_data is {tc['valid_data']} and the version is equal to {tc['version']}"
        else:
            assert (
                validator().get_valid_values_set() == tc["expected_result"]
            ), f"While we test {tc['name']}, the returned data is not equal to {tc['expected_result']} when the valid_data is {tc['valid_data']} and the version is equal to {tc['version']}"
