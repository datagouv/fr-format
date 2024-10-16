from frformat import Canton, CodeRegion, Commune, Region
from frformat.geo_enum_format import Millesime


def test_code_region():
    code_region_2023 = CodeRegion(Millesime.A2023)
    code_region_2024 = CodeRegion(Millesime.A2024)

    valid_test_cases = ["01", "75"]
    invalid_test_cases = ["AA", "00"]
    for tc in valid_test_cases:
        assert code_region_2023.is_valid(tc)
        assert code_region_2024.is_valid(tc)

    for tc in invalid_test_cases:
        assert not code_region_2023.is_valid(tc)
        assert not code_region_2024.is_valid(tc)


def test_region():
    region_2023 = Region(Millesime.A2023)
    region_2024 = Region(Millesime.A2024)

    valid_test_cases = ["Centre-Val de Loire", "La Réunion", "Corse"]
    invalid_test_cases = ["Beleriand", "Canyon Cosmo"]
    for tc in valid_test_cases:
        assert region_2023.is_valid(tc)
        assert region_2024.is_valid(tc)

    for tc in invalid_test_cases:
        assert not region_2023.is_valid(tc)
        assert not region_2024.is_valid(tc)


def test_commune():
    commune_2023 = Commune(Millesime.A2023)
    commune_2024 = Commune(Millesime.A2024)

    valid_test_cases_cog_2023 = [
        "La Chapelle-Achard",
        "Beaumont-les-Nonains",
        "La Moncelle",
        "Montestrucq",
    ]
    invalid_test_cases_cog_2023 = [
        "Costa del Sol",
        "Val-d'Usiers",
        "La Chapelle-Fleurigné",
        "Oullins-Pierre-Bénite",
    ]

    valid_test_cases_cog_2024 = [
        "Oullins-Pierre-Bénite",
        "Bellac",
        "Val-d'Usiers",
        "La Chapelle-Fleurigné",
    ]
    invalid_test_cases_cog_2024 = [
        "Costa del Sol",
        "Montestrucq",
        "La Chapelle-Achard",
        "Senonville",
    ]

    for tc in valid_test_cases_cog_2023:
        assert commune_2023.is_valid(tc)

    for tc in invalid_test_cases_cog_2023:
        assert not commune_2023.is_valid(tc)

    for tc in valid_test_cases_cog_2024:
        assert commune_2024.is_valid(tc)

    for tc in invalid_test_cases_cog_2024:
        assert not commune_2024.is_valid(tc)


def test_canton():
    canton_2023 = Canton(Millesime.A2023)
    canton_2024 = Canton(Millesime.A2024)

    valid_test_cases_cog_2023 = [
        "Lagnieu",
        "Meximieux",
    ]
    invalid_test_cases_cog_2023 = ["Paris", "Lyon"]

    valid_test_cases_cog_2024 = ["Paris", "Lyon"]
    invalid_test_cases_cog_2024 = [
        "Saint Quentin",
    ]

    for tc in valid_test_cases_cog_2023:
        assert canton_2023.is_valid(tc)

    for tc in invalid_test_cases_cog_2023:
        assert not canton_2023.is_valid(tc)

    for tc in valid_test_cases_cog_2024:
        assert canton_2024.is_valid(tc)

    for tc in invalid_test_cases_cog_2024:
        assert not canton_2024.is_valid(tc)
