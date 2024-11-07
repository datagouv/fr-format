from frformat import (
    Canton,
    CodeCommuneInsee,
    CodePaysISO2,
    CodePaysISO3,
    CodeRegion,
    Commune,
    Departement,
    Millesime,
    NumeroDepartement,
    Pays,
    Region,
)


def test_code_region():
    code_region_2023 = CodeRegion(Millesime.A2023)
    code_region_2024 = CodeRegion(Millesime.A2024)
    last_code_region = CodeRegion(Millesime.LATEST)

    valid_test_cases = ["01", "75"]
    invalid_test_cases = ["AA", "00", "7 5"]
    for tc in valid_test_cases:
        assert code_region_2023.is_valid(tc)
        assert code_region_2024.is_valid(tc)
        assert last_code_region.is_valid(tc)

    for tc in invalid_test_cases:
        assert not code_region_2023.is_valid(tc)
        assert not code_region_2024.is_valid(tc)
        assert not last_code_region.is_valid(tc)


def test_region():
    region_2023 = Region(Millesime.A2023)
    region_2024 = Region(Millesime.A2024)
    last_region = Region(Millesime.LATEST)

    valid_test_cases = ["Centre-Val de Loire", "La Réunion", "Corse"]
    invalid_test_cases = [
        "Beleriand",
        "Canyon Cosmo",
        "corse",
        "Centre val de Loire",
        "la reunion",
    ]
    for tc in valid_test_cases:
        assert region_2023.is_valid(tc)
        assert region_2024.is_valid(tc)
        assert last_region.is_valid(tc)

    for tc in invalid_test_cases:
        assert not region_2023.is_valid(tc)
        assert not region_2024.is_valid(tc)
        assert not last_region.is_valid(tc)


def test_commune():
    commune_2023 = Commune(Millesime.A2023)
    commune_2024 = Commune(Millesime.A2024)
    last_commune = Commune(Millesime.LATEST)

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
        "la chapelle Fleurigne",
        "Costa-del Sol",
    ]

    valid_test_cases_cog_2024 = [
        "Oullins-Pierre-Bénite",
        "Bellac",
        "Val-d'Usiers",
        "La Chapelle-Fleurigné",
    ]

    valid_test_cases_last_cog = valid_test_cases_cog_2024

    invalid_test_cases_cog_2024 = [
        "Costa del Sol",
        "Montestrucq",
        "La Chapelle-Achard",
        "Senonville",
        "montestrucq",
        "La Chapelle     Achard",
    ]

    invalid_test_cases_last_cog = invalid_test_cases_cog_2024

    for tc in valid_test_cases_cog_2023:
        assert commune_2023.is_valid(tc)

    for tc in invalid_test_cases_cog_2023:
        assert not commune_2023.is_valid(tc)

    for tc in valid_test_cases_cog_2024:
        assert commune_2024.is_valid(tc)

    for tc in invalid_test_cases_cog_2024:
        assert not commune_2024.is_valid(tc)

    for tc in valid_test_cases_last_cog:
        assert last_commune.is_valid(tc)

    for tc in invalid_test_cases_last_cog:
        assert not last_commune.is_valid(tc)


def test_canton():
    canton_2023 = Canton(Millesime.A2023)
    canton_2024 = Canton(Millesime.A2024)
    last_canton = Canton(Millesime.LATEST)

    valid_test_cases_cog_2023 = [
        "Lagnieu",
        "Meximieux",
    ]
    invalid_test_cases_cog_2023 = ["Paris", "Lyon", "paris"]

    valid_test_cases_cog_2024 = ["Paris", "Lyon"]
    valid_test_cases_last_cog = valid_test_cases_cog_2024

    invalid_test_cases_cog_2024 = ["Saint Quentin", "saint  quentin"]
    invalid_test_cases_last_cog = invalid_test_cases_cog_2024

    for tc in valid_test_cases_cog_2023:
        assert canton_2023.is_valid(tc)

    for tc in invalid_test_cases_cog_2023:
        assert not canton_2023.is_valid(tc)

    for tc in valid_test_cases_cog_2024:
        assert canton_2024.is_valid(tc)

    for tc in invalid_test_cases_cog_2024:
        assert not canton_2024.is_valid(tc)

    for tc in valid_test_cases_last_cog:
        assert last_canton.is_valid(tc)

    for tc in invalid_test_cases_last_cog:
        assert not last_canton.is_valid(tc)


def test_code_pays():
    code_pays_2023_IS02 = CodePaysISO2(Millesime.A2023)
    code_pays_2024_IS02 = CodePaysISO2(Millesime.A2024)
    last_code_pays_IS02 = CodePaysISO2(Millesime.LATEST)

    code_pays_2023_IS03 = CodePaysISO3(Millesime.A2023)
    code_pays_2024_IS03 = CodePaysISO3(Millesime.A2024)
    last_code_pays_IS03 = CodePaysISO3(Millesime.LATEST)

    valid_test_cases_iso2_cog_2023 = ["BV", "SJ"]
    invalid_test_cases_iso2_cog_2023 = ["RWA", "TCD", "rwa"]

    valid_test_cases_iso2_cog_2024 = ["FR", "JP"]
    invalid_test_cases_iso2_cog_2024 = ["BV", "SJ", "bv"]

    valid_test_cases_iso2_last_cog = valid_test_cases_iso2_cog_2024
    invalid_test_cases_iso2_last_cog = invalid_test_cases_iso2_cog_2024

    valid_test_cases_iso3_cog_2023 = ["BVT", "SJM"]
    invalid_test_cases_iso3_cog_2023 = ["BF", "GH", "gh"]

    valid_test_cases_iso3_cog_2024 = ["FRA", "JPN"]
    invalid_test_cases_iso3_cog_2024 = ["BVT", "SJM", "bvt"]

    valid_test_cases_iso3_last_cog = valid_test_cases_iso3_cog_2024
    invalid_test_cases_iso3_last_cog = invalid_test_cases_iso3_cog_2024

    for tc in valid_test_cases_iso2_cog_2023:
        assert code_pays_2023_IS02.is_valid(tc)

    for tc in invalid_test_cases_iso2_cog_2023:
        assert not code_pays_2023_IS02.is_valid(tc)

    for tc in valid_test_cases_iso2_cog_2024:
        assert code_pays_2024_IS02.is_valid(tc)

    for tc in invalid_test_cases_iso2_cog_2024:
        assert not code_pays_2024_IS02.is_valid(tc)

    for tc in valid_test_cases_iso2_last_cog:
        assert last_code_pays_IS02.is_valid(tc)

    for tc in invalid_test_cases_iso2_last_cog:
        assert not last_code_pays_IS02.is_valid(tc)

    for tc in valid_test_cases_iso3_cog_2023:
        assert code_pays_2023_IS03.is_valid(tc)

    for tc in invalid_test_cases_iso3_cog_2023:
        assert not code_pays_2023_IS03.is_valid(tc)

    for tc in valid_test_cases_iso3_cog_2024:
        assert code_pays_2024_IS03.is_valid(tc)

    for tc in invalid_test_cases_iso3_cog_2024:
        assert not code_pays_2024_IS03.is_valid(tc)

    for tc in valid_test_cases_iso3_last_cog:
        assert last_code_pays_IS03.is_valid(tc)

    for tc in invalid_test_cases_iso3_last_cog:
        assert not last_code_pays_IS03.is_valid(tc)


def test_code_commune_insee():
    code_commune_insee_cog_2023 = CodeCommuneInsee(Millesime.A2023)
    code_commune_insee_cog_2024 = CodeCommuneInsee(Millesime.A2024)
    last_code_commune_insee = CodeCommuneInsee(Millesime.LATEST)

    cog_2023_value = "01015"
    assert code_commune_insee_cog_2023.is_valid(cog_2023_value)
    assert code_commune_insee_cog_2023.format(cog_2023_value) == cog_2023_value
    assert code_commune_insee_cog_2023.is_valid("2B002")

    cog_2023_invalid_values = ["77777", "  01015"]
    for iv in cog_2023_invalid_values:
        assert not code_commune_insee_cog_2023.is_valid(iv)

    cog_2024_value = "64300"
    last_cog_value = cog_2024_value

    assert code_commune_insee_cog_2024.is_valid(cog_2024_value)
    assert code_commune_insee_cog_2024.format(cog_2024_value) == cog_2024_value
    assert code_commune_insee_cog_2024.is_valid("2A331")

    assert last_code_commune_insee.is_valid(last_cog_value)
    assert last_code_commune_insee.format(last_cog_value) == last_cog_value

    cog_2024_invalid_values = ["64402", "64  300"]
    invalid_last_cog_values = cog_2024_invalid_values

    for iv in cog_2024_invalid_values:
        assert not code_commune_insee_cog_2024.is_valid(iv)

    for iv in invalid_last_cog_values:
        assert not last_code_commune_insee.is_valid(iv)


def test_departement():
    departement_cog_2023 = Departement(Millesime.A2023)
    departement_cog_2024 = Departement(Millesime.A2024)
    last_departement_cog = Departement(Millesime.LATEST)

    valid_test_cases = ["Alpes-Maritimes", "Gard", "Mayotte", "Vendée"]
    invalid_test_cases = ["Charente-Inférieure", "Vendee", "Alpes  maritimes"]

    for tc in valid_test_cases:
        assert departement_cog_2023.is_valid(tc)
        assert departement_cog_2024.is_valid(tc)
        assert last_departement_cog.is_valid(tc)

    for tc in invalid_test_cases:
        assert not departement_cog_2023.is_valid(tc)
        assert not departement_cog_2024.is_valid(tc)
        assert not last_departement_cog.is_valid(tc)


def test_pays():
    pays_cog_2024 = Pays(Millesime.A2024)
    last_pays_cog = Pays(Millesime.LATEST)

    valid_pays_cog_2024 = ["France", "Pays-Bas", "Bosnie-Herzégovine"]
    invalid_pays_cog_2024 = ["L'Eldorado", "Zubrowska", "Pays Bas", "france"]

    valid_last_pays_cog = valid_pays_cog_2024
    invalid_last_pays_cog = invalid_pays_cog_2024

    for tc in valid_pays_cog_2024:
        assert pays_cog_2024.is_valid(tc)

    for tc in invalid_pays_cog_2024:
        assert not pays_cog_2024.is_valid(tc)

    for tc in valid_last_pays_cog:
        assert last_pays_cog.is_valid(tc)

    for tc in invalid_last_pays_cog:
        assert not last_pays_cog.is_valid(tc)


def test_numero_departement():
    num_departement_cog_2023 = NumeroDepartement(Millesime.A2023)
    num_departement_cog_2024 = NumeroDepartement(Millesime.A2024)
    last_num_departement_cog = NumeroDepartement(Millesime.LATEST)

    num_departement_valid = ["05", "2B", "974"]
    num_departement_invalid = ["99", "051", "2b", "  97 4"]

    for tc in num_departement_valid:
        assert num_departement_cog_2023.is_valid(tc)
        assert num_departement_cog_2024.is_valid(tc)
        assert last_num_departement_cog.is_valid(tc)

    for tc in num_departement_invalid:
        assert not num_departement_cog_2023.is_valid(tc)
        assert not num_departement_cog_2024.is_valid(tc)
        assert not last_num_departement_cog.is_valid(tc)
