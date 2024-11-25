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


class ValidatorTest:
    def __init__(self, cog, testCases, formatClass):
        self.cog = cog
        self.testCases = testCases
        self.formatClass = formatClass

    def test_valid_cases(self):
        for tc in self.testCases.get("valid", []):
            assert self.formatClass(self.cog).is_valid(tc)

    def test_invalid_cases(self):
        for tc in self.testCases.get("invalid", []):
            assert not self.formatClass(self.cog).is_valid(tc)

    def run_all_tests(self):
        self.test_valid_cases()
        self.test_invalid_cases()


def test_all_validator():
    validator_details = [
        {
            "name": "CodeRegion",
            "cog": Millesime.M2023,
            "formatClass": CodeRegion,
            "test_cases": {"valid": ["01", "75"], "invalid": ["AA", "00", "7 5"]},
        },
        {
            "name": "CodeRegion",
            "cog": Millesime.M2024,
            "formatClass": CodeRegion,
            "test_cases": {"valid": ["01", "75"], "invalid": ["AA", "00", "7 5"]},
        },
    ]

    for vd in validator_details:
        validatorTest = ValidatorTest(vd["cog"], vd["test_cases"], vd["formatClass"])
        validatorTest.run_all_tests()


""" def test_code_region():
    validatorTest2023 = ValidatorTest(
        Millesime.M2023, ["01", "75"], ["AA", "00", "7 5"], CodeRegion
    )

    validatorTest2024 = ValidatorTest(
        Millesime.M2024, ["01", "75"], ["AA", "00", "7 5"], CodeRegion
    )

    validatorTest2023.test_valid_cases()
    validatorTest2023.test_invalid_cases()

    validatorTest2024.test_valid_cases()
    validatorTest2024.test_invalid_cases() """


def test_region():
    region_2023 = Region(Millesime.M2023)
    region_2024 = Region(Millesime.M2024)

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

    for tc in invalid_test_cases:
        assert not region_2023.is_valid(tc)
        assert not region_2024.is_valid(tc)


def test_commune():
    commune_2023 = Commune(Millesime.M2023)
    commune_2024 = Commune(Millesime.M2024)

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

    invalid_test_cases_cog_2024 = [
        "Costa del Sol",
        "Montestrucq",
        "La Chapelle-Achard",
        "Senonville",
        "montestrucq",
        "La Chapelle     Achard",
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
    canton_2023 = Canton(Millesime.M2023)
    canton_2024 = Canton(Millesime.M2024)

    valid_test_cases_cog_2023 = [
        "Lagnieu",
        "Meximieux",
    ]
    invalid_test_cases_cog_2023 = ["Paris", "Lyon", "paris"]

    valid_test_cases_cog_2024 = ["Paris", "Lyon"]

    invalid_test_cases_cog_2024 = ["Saint Quentin", "saint  quentin"]

    for tc in valid_test_cases_cog_2023:
        assert canton_2023.is_valid(tc)

    for tc in invalid_test_cases_cog_2023:
        assert not canton_2023.is_valid(tc)

    for tc in valid_test_cases_cog_2024:
        assert canton_2024.is_valid(tc)

    for tc in invalid_test_cases_cog_2024:
        assert not canton_2024.is_valid(tc)


def test_code_pays():
    code_pays_2023_IS02 = CodePaysISO2(Millesime.M2023)
    code_pays_2024_IS02 = CodePaysISO2(Millesime.M2024)

    code_pays_2023_IS03 = CodePaysISO3(Millesime.M2023)
    code_pays_2024_IS03 = CodePaysISO3(Millesime.M2024)

    valid_test_cases_iso2_cog_2023 = ["BV", "SJ"]
    invalid_test_cases_iso2_cog_2023 = ["RWA", "TCD", "rwa"]

    valid_test_cases_iso2_cog_2024 = ["FR", "JP"]
    invalid_test_cases_iso2_cog_2024 = ["BV", "SJ", "bv"]

    valid_test_cases_iso3_cog_2023 = ["BVT", "SJM"]
    invalid_test_cases_iso3_cog_2023 = ["BF", "GH", "gh"]

    valid_test_cases_iso3_cog_2024 = ["FRA", "JPN"]
    invalid_test_cases_iso3_cog_2024 = ["BVT", "SJM", "bvt"]

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
    code_commune_insee_cog_2023 = CodeCommuneInsee(Millesime.M2023)
    code_commune_insee_cog_2024 = CodeCommuneInsee(Millesime.M2024)

    cog_2023_value = "01015"
    assert code_commune_insee_cog_2023.is_valid(cog_2023_value)
    assert code_commune_insee_cog_2023.format(cog_2023_value) == cog_2023_value
    assert code_commune_insee_cog_2023.is_valid("2B002")

    cog_2023_invalid_values = ["77777", "  01015"]
    for iv in cog_2023_invalid_values:
        assert not code_commune_insee_cog_2023.is_valid(iv)

    cog_2024_value = "64300"

    assert code_commune_insee_cog_2024.is_valid(cog_2024_value)
    assert code_commune_insee_cog_2024.format(cog_2024_value) == cog_2024_value
    assert code_commune_insee_cog_2024.is_valid("2A331")

    cog_2024_invalid_values = ["64402", "64  300"]

    for iv in cog_2024_invalid_values:
        assert not code_commune_insee_cog_2024.is_valid(iv)


def test_departement():
    departement_cog_2023 = Departement(Millesime.M2023)
    departement_cog_2024 = Departement(Millesime.M2024)

    valid_test_cases = ["Alpes-Maritimes", "Gard", "Mayotte", "Vendée"]
    invalid_test_cases = ["Charente-Inférieure", "Vendee", "Alpes  maritimes"]

    for tc in valid_test_cases:
        assert departement_cog_2023.is_valid(tc)
        assert departement_cog_2024.is_valid(tc)

    for tc in invalid_test_cases:
        assert not departement_cog_2023.is_valid(tc)
        assert not departement_cog_2024.is_valid(tc)


def test_pays():
    pays_cog_2024 = Pays(Millesime.M2024)

    valid_pays_cog_2024 = ["France", "Pays-Bas", "Bosnie-Herzégovine"]
    invalid_pays_cog_2024 = ["L'Eldorado", "Zubrowska", "Pays Bas", "france"]

    for tc in valid_pays_cog_2024:
        assert pays_cog_2024.is_valid(tc)

    for tc in invalid_pays_cog_2024:
        assert not pays_cog_2024.is_valid(tc)


def test_numero_departement():
    num_departement_cog_2023 = NumeroDepartement(Millesime.M2023)
    num_departement_cog_2024 = NumeroDepartement(Millesime.M2024)

    num_departement_valid = ["05", "2B", "974"]
    num_departement_invalid = ["99", "051", "2b", "  97 4"]

    for tc in num_departement_valid:
        assert num_departement_cog_2023.is_valid(tc)
        assert num_departement_cog_2024.is_valid(tc)

    for tc in num_departement_invalid:
        assert not num_departement_cog_2023.is_valid(tc)
        assert not num_departement_cog_2024.is_valid(tc)
