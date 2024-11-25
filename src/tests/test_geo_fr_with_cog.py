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
        {
            "name": "Region",
            "cog": Millesime.M2023,
            "formatClass": Region,
            "test_cases": {
                "valid": ["Centre-Val de Loire", "La Réunion", "Corse"],
                "invalid": [
                    "Beleriand",
                    "Canyon Cosmo",
                    "corse",
                    "Centre val de Loire",
                    "la reunion",
                ],
            },
        },
        {
            "name": "Region",
            "cog": Millesime.M2024,
            "formatClass": Region,
            "test_cases": {
                "valid": ["Centre-Val de Loire", "La Réunion", "Corse"],
                "invalid": [
                    "Beleriand",
                    "Canyon Cosmo",
                    "corse",
                    "Centre val de Loire",
                    "la reunion",
                ],
            },
        },
        {
            "name": "Commune",
            "cog": Millesime.M2023,
            "formatClass": Commune,
            "test_cases": {
                "valid": [
                    "La Chapelle-Achard",
                    "Beaumont-les-Nonains",
                    "La Moncelle",
                    "Montestrucq",
                ],
                "invalid": [
                    "Costa del Sol",
                    "Val-d'Usiers",
                    "La Chapelle-Fleurigné",
                    "Oullins-Pierre-Bénite",
                    "la chapelle Fleurigne",
                    "Costa-del Sol",
                ],
            },
        },
        {
            "name": "Commune",
            "cog": Millesime.M2024,
            "formatClass": Commune,
            "test_cases": {
                "valid": [
                    "Oullins-Pierre-Bénite",
                    "Bellac",
                    "Val-d'Usiers",
                    "La Chapelle-Fleurigné",
                ],
                "invalid": [
                    "Costa del Sol",
                    "Montestrucq",
                    "La Chapelle-Achard",
                    "Senonville",
                    "montestrucq",
                    "La Chapelle     Achard",
                ],
            },
        },
        {
            "name": "Canton",
            "cog": Millesime.M2023,
            "formatClass": Canton,
            "test_cases": {
                "valid": [
                    "Lagnieu",
                    "Meximieux",
                ],
                "invalid": ["Paris", "Lyon", "paris"],
            },
        },
        {
            "name": "Canton",
            "cog": Millesime.M2024,
            "formatClass": Canton,
            "test_cases": {
                "valid": ["Paris", "Lyon"],
                "invalid": ["Saint Quentin", "saint  quentin"],
            },
        },
        {
            "name": "CodePaysISO2",
            "cog": Millesime.M2023,
            "formatClass": CodePaysISO2,
            "test_cases": {"valid": ["BV", "SJ"], "invalid": ["RWA", "TCD", "rwa"]},
        },
        {
            "name": "CodePaysISO2",
            "cog": Millesime.M2024,
            "formatClass": CodePaysISO2,
            "test_cases": {"valid": ["FR", "JP"], "invalid": ["BV", "SJ", "bv"]},
        },
        {
            "name": "CodePaysISO3",
            "cog": Millesime.M2023,
            "formatClass": CodePaysISO3,
            "test_cases": {"valid": ["BVT", "SJM"], "invalid": ["BF", "GH", "gh"]},
        },
        {
            "name": "CodePaysISO3",
            "cog": Millesime.M2024,
            "formatClass": CodePaysISO3,
            "test_cases": {"valid": ["FRA", "JPN"], "invalid": ["BVT", "SJM", "bvt"]},
        },
        {
            "name": "Departement",
            "cog": Millesime.M2023,
            "formatClass": Departement,
            "test_cases": {
                "valid": ["Alpes-Maritimes", "Gard", "Mayotte", "Vendée"],
                "invalid": ["Charente-Inférieure", "Vendee", "Alpes  maritimes"],
            },
        },
        {
            "name": "Departement",
            "cog": Millesime.M2024,
            "formatClass": Departement,
            "test_cases": {
                "valid": ["Alpes-Maritimes", "Gard", "Mayotte", "Vendée"],
                "invalid": ["Charente-Inférieure", "Vendee", "Alpes  maritimes"],
            },
        },
        {
            "name": "Pays",
            "cog": Millesime.M2024,
            "formatClass": Pays,
            "test_cases": {
                "valid": ["France", "Pays-Bas", "Bosnie-Herzégovine"],
                "invalid": ["L'Eldorado", "Zubrowska", "Pays Bas", "france"],
            },
        },
    ]

    for vd in validator_details:
        validatorTest = ValidatorTest(vd["cog"], vd["test_cases"], vd["formatClass"])
        validatorTest.run_all_tests()


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
