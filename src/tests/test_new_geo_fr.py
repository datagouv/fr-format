from frformat import CodeRegion, Commune, Region
from frformat.geo_enum_format import Millesime
from tests.geo_testing import strict_lenient_test_helper_factory


def test_code_region():
    _test_code_region = strict_lenient_test_helper_factory(CodeRegion)

    code_region_strict = ["01", "75"]
    code_region_lenient = []
    code_region_invalid = ["AA", "00"]

    _test_code_region(code_region_strict, code_region_lenient, code_region_invalid)


def test_region():
    _test_region = strict_lenient_test_helper_factory(Region)

    region_strict = ["Centre-Val de Loire", "La Réunion", "Corse"]
    region_lenient = ["Centre Val de Loire", "La Reunion", "corse"]
    region_invalid = ["Beleriand", "Canyon Cosmo"]

    _test_region(region_strict, region_lenient, region_invalid)


def test_commune():
    commune_2023 = Commune(Millesime.A2023)
    commune_2024 = Commune(Millesime.A2024)

    valid_test_cases_cog_2023 = [
        "Bellac",
        "Beaumont-les-Nonains",
        "La Moncelle",
        "Urdès",
    ]
    invalid_test_cases_cog_2023 = [
        "Costa del Sol",
        "Val-d’Usiers",
        "La Chapelle-Fleurigné",
    ]

    valid_test_cases_cog_2024 = [
        "Beaumont-les-Nonains",
        "Bellac",
        "Val-d’Usiers",
        "La Chapelle-Fleurigné",
    ]
    invalid_test_cases_cog_2024 = ["Costa del Sol", "La Moncelle", "Urdès"]

    for tc in valid_test_cases_cog_2023:
        assert commune_2023.is_valid(tc)

    for tc in invalid_test_cases_cog_2023:
        assert not commune_2023.is_valid(tc)

    for tc in valid_test_cases_cog_2024:
        assert commune_2024.is_valid(tc)

    for tc in invalid_test_cases_cog_2024:
        assert not commune_2024.is_valid(tc)
