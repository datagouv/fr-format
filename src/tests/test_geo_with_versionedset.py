import pytest

from frformat.geo_enum_format import Millesime, new
from frformat.versioned_set import VersionedSet


def test_geo_enum_format_with_versionning():
    versioned_data = VersionedSet()
    versioned_data.add_version(
        Millesime.M2023,
        frozenset({"Ambléon", "Ambronay"}),
    )
    versioned_data.add_version(Millesime.M2024, frozenset({"Arandas"}))

    FormatTest = new(
        "FormatTest", "Versionned format", "Versionned format", versioned_data
    )
    format_M2023 = FormatTest(Millesime.M2023)
    format_M2024 = FormatTest(Millesime.M2024)
    format_latest = FormatTest(Millesime.LATEST)

    # Valid value M2023
    assert format_M2023.is_valid("Ambléon")

    # Invalid value M2023
    assert not format_M2023.is_valid("Anglefort")

    # Valid value M2024
    assert format_M2024.is_valid("Arandas")

    # latest
    assert format_latest.is_valid("Arandas")
    assert not format_latest.is_valid("Ambléon")

    # Test with a non-existent version
    with pytest.raises(ValueError):
        FormatTest("2025")


def test_geo_enum_format_with_empty_data():
    versioned_data = VersionedSet()
    versioned_data.add_version(
        Millesime.M2023,
        frozenset({}),
    )
    FormatTest = new(
        "FormatTest", "Versionned format", "Versionned format", versioned_data
    )

    with pytest.raises(ValueError):
        FormatTest(Millesime.M2023)
