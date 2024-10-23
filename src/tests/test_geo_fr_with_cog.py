from frformat import (
    Canton,
    CodeCommuneInsee,
    CodePaysISO2,
    CodePaysISO3,
    CodeRegion,
    Commune,
    Departement,
    Pays,
    Region,
)
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


def test_code_pays():
    code_pays_2023_IS02 = CodePaysISO2(Millesime.A2023)
    code_pays_2024_IS02 = CodePaysISO2(Millesime.A2024)
    code_pays_2023_IS03 = CodePaysISO3(Millesime.A2023)
    code_pays_2024_IS03 = CodePaysISO3(Millesime.A2024)

    valid_test_cases_iso2_cog_2023 = ["BV", "SJ"]
    invalid_test_cases_iso2_cog_2023 = ["RWA", "TCD"]

    valid_test_cases_iso2_cog_2024 = ["FR", "JP"]
    invalid_test_cases_iso2_cog_2024 = ["BV", "SJ"]

    valid_test_cases_iso3_cog_2023 = ["BVT", "SJM"]
    invalid_test_cases_iso3_cog_2023 = ["BF", "GH"]

    valid_test_cases_iso3_cog_2024 = ["FRA", "JPN"]
    invalid_test_cases_iso3_cog_2024 = ["BVT", "SJM"]

    for tc in valid_test_cases_iso2_cog_2023:
        assert code_pays_2023_IS02.is_valid(tc)

    for tc in invalid_test_cases_iso2_cog_2023:
        assert not code_pays_2023_IS02.is_valid(tc)

    for tc in valid_test_cases_iso2_cog_2024:
        assert code_pays_2024_IS02.is_valid(tc)

    for tc in invalid_test_cases_iso2_cog_2024:
        assert not code_pays_2024_IS02.is_valid(tc)

    for tc in valid_test_cases_iso3_cog_2023:
        assert code_pays_2023_IS03.is_valid(tc)

    for tc in invalid_test_cases_iso3_cog_2023:
        assert not code_pays_2023_IS03.is_valid(tc)

    for tc in valid_test_cases_iso3_cog_2024:
        assert code_pays_2024_IS03.is_valid(tc)

    for tc in invalid_test_cases_iso3_cog_2024:
        assert not code_pays_2024_IS03.is_valid(tc)


def test_code_commune_insee():
    code_commune_insee_cog_2023 = CodeCommuneInsee(Millesime.A2023)
    code_commune_insee_cog_2024 = CodeCommuneInsee(Millesime.A2024)

    cog_2023_value = "01015"
    assert code_commune_insee_cog_2023.is_valid(cog_2023_value)
    assert code_commune_insee_cog_2023.format(cog_2023_value) == cog_2023_value
    assert code_commune_insee_cog_2023.is_valid("2B002")

    assert not code_commune_insee_cog_2023.is_valid("77777")

    cog_2024_value = "64300"
    assert code_commune_insee_cog_2024.is_valid(cog_2024_value)
    assert code_commune_insee_cog_2024.format(cog_2024_value) == cog_2024_value
    assert code_commune_insee_cog_2024.is_valid("2A331")

    assert not code_commune_insee_cog_2024.is_valid("64402")


def test_departement():
    departement_cog_2023 = Departement(Millesime.A2023)
    departement_cog_2024 = Departement(Millesime.A2024)

    valid_test_cases = ["Alpes-Maritimes", "Gard", "Mayotte", "Vendée"]
    invalid_test_cases = ["Charente-Inférieure"]

    for tc in valid_test_cases:
        assert departement_cog_2023.is_valid(tc)
        assert departement_cog_2024.is_valid(tc)

    for tc in invalid_test_cases:
        assert not departement_cog_2023.is_valid(tc)
        assert not departement_cog_2024.is_valid(tc)


def test_pays():
    pays_cog_2024 = Pays(Millesime.A2024)

    valid_pays_cog_2024 = ["France", "Pays-Bas", "Bosnie-Herzégovine"]
    invalid_pays_cog_2024 = ["L'Eldorado", "Zubrowska"]

    for tc in valid_pays_cog_2024:
        assert pays_cog_2024.is_valid(tc)

    for tc in invalid_pays_cog_2024:
        assert not pays_cog_2024.is_valid(tc)
