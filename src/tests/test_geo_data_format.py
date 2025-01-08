import pytest

from frformat.geo_format import Millesime, new
from frformat.versioned_set import VersionedSet


def test_geo_data_format():
    versioned_data = VersionedSet[Millesime]()
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

    # Test with a non-existent/invalid version
    with pytest.raises(ValueError):
        FormatTest("2025")
