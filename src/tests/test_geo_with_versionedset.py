import pytest

from frformat.geo_enum_format_with_versionedset import Millesime, new
from frformat.versioned_set import VersionedSet


def test_geo_enum_format_versionned():
    versioned_data = VersionedSet()
    versioned_data.add_version(
        Millesime.M2023,
        frozenset({"Ambléon", "Ambronay", "Ambutrix", "Andert-et-Condon"}),
    )
    versioned_data.add_version(
        Millesime.M2024, frozenset({"Anglefort", "Apremont", "Aranc", "Arandas"})
    )

    FormatTest = new(
        "FormatTest", "Versionned format", "Versionned format", versioned_data
    )
    format_M2023 = FormatTest(Millesime.M2023)
    format_M2024 = FormatTest(Millesime.M2024)
    format_latest = FormatTest(Millesime("latest"))
    # Valid value M2023
    assert format_M2023.is_valid("Ambléon")

    # Invalid value M2023
    assert not format_M2023.is_valid("Anglefort")

    # Valid value M2024
    assert format_M2024.is_valid("Arandas")

    # Invalid version
    with pytest.raises(ValueError):
        FormatTest(Millesime.M2025)  # Test with a non-existent version

    # latest
    assert format_latest.is_valid("Aranc")
    assert not format_latest.is_valid("Ambléon")
