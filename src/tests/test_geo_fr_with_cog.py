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
    def __init__(self, cog, validTestCases, invalidTestCases, formatClass):
        self.cog = cog
        self.validTestCases = validTestCases
        self.invalidTestCases = invalidTestCases
        self.formatClass = formatClass

    def test_valid_cases(self):
        for tc in self.validTestCases:
            assert self.formatClass(self.cog).is_valid(tc)

    def test_invalid_cases(self):
        for tc in self.invalidTestCases:
            assert not self.formatClass(self.cog).is_valid(tc)

    def run_all_tests(self):
        self.test_valid_cases()
        self.test_invalid_cases()


def test_all_validators_with_cog():
    test_cases = [
        {
            "name": "CodeRegion",
            "cog": Millesime.M2023,
            "formatClass": CodeRegion,
            "validTestCases": ["01", "75"],
            "invalidTestCases": ["AA", "00", "7 5"],
        },
        {
            "name": "CodeRegion",
            "cog": Millesime.M2024,
            "formatClass": CodeRegion,
            "validTestCases": ["01", "75"],
            "invalidTestCases": ["AA", "00", "7 5"],
        },
        {
            "name": "Region",
            "cog": Millesime.M2023,
            "formatClass": Region,
            "validTestCases": ["Centre-Val de Loire", "La Réunion", "Corse"],
            "invalidTestCases": [
                "Beleriand",
                "Canyon Cosmo",
                "corse",
                "Centre val de Loire",
                "la reunion",
            ],
        },
        {
            "name": "Region",
            "cog": Millesime.M2024,
            "formatClass": Region,
            "validTestCases": ["Centre-Val de Loire", "La Réunion", "Corse"],
            "invalidTestCases": [
                "Beleriand",
                "Canyon Cosmo",
                "corse",
                "Centre val de Loire",
                "la reunion",
            ],
        },
        {
            "name": "Commune",
            "cog": Millesime.M2023,
            "formatClass": Commune,
            "validTestCases": [
                "La Chapelle-Achard",
                "Beaumont-les-Nonains",
                "La Moncelle",
                "Montestrucq",
            ],
            "invalidTestCases": [
                "Costa del Sol",
                "Val-d'Usiers",
                "La Chapelle-Fleurigné",
                "Oullins-Pierre-Bénite",
                "la chapelle Fleurigne",
                "Costa-del Sol",
            ],
        },
        {
            "name": "Commune",
            "cog": Millesime.M2024,
            "formatClass": Commune,
            "validTestCases": [
                "Oullins-Pierre-Bénite",
                "Bellac",
                "Val-d'Usiers",
                "La Chapelle-Fleurigné",
            ],
            "invalidTestCases": [
                "Costa del Sol",
                "Montestrucq",
                "La Chapelle-Achard",
                "Senonville",
                "montestrucq",
                "La Chapelle     Achard",
            ],
        },
        {
            "name": "Canton",
            "cog": Millesime.M2023,
            "formatClass": Canton,
            "validTestCases": [
                "Lagnieu",
                "Meximieux",
            ],
            "invalidTestCases": ["Paris", "Lyon", "paris"],
        },
        {
            "name": "Canton",
            "cog": Millesime.M2024,
            "formatClass": Canton,
            "validTestCases": ["Paris", "Lyon"],
            "invalidTestCases": ["Saint Quentin", "saint  quentin"],
        },
        {
            "name": "CodePaysISO2",
            "cog": Millesime.M2023,
            "formatClass": CodePaysISO2,
            "validTestCases": ["BV", "SJ"],
            "invalidTestCases": ["RWA", "TCD", "rwa"],
        },
        {
            "name": "CodePaysISO2",
            "cog": Millesime.M2024,
            "formatClass": CodePaysISO2,
            "validTestCases": ["FR", "JP"],
            "invalidTestCases": ["BV", "SJ", "bv"],
        },
        {
            "name": "CodePaysISO3",
            "cog": Millesime.M2023,
            "formatClass": CodePaysISO3,
            "validTestCases": ["BVT", "SJM"],
            "invalidTestCases": ["BF", "GH", "gh"],
        },
        {
            "name": "CodePaysISO3",
            "cog": Millesime.M2024,
            "formatClass": CodePaysISO3,
            "validTestCases": ["FRA", "JPN"],
            "invalidTestCases": ["BVT", "SJM", "bvt"],
        },
        {
            "name": "Departement",
            "cog": Millesime.M2023,
            "formatClass": Departement,
            "validTestCases": ["Alpes-Maritimes", "Gard", "Mayotte", "Vendée"],
            "invalidTestCases": ["Charente-Inférieure", "Vendee", "Alpes  maritimes"],
        },
        {
            "name": "Departement",
            "cog": Millesime.M2024,
            "formatClass": Departement,
            "validTestCases": ["Alpes-Maritimes", "Gard", "Mayotte", "Vendée"],
            "invalidTestCases": ["Charente-Inférieure", "Vendee", "Alpes  maritimes"],
        },
        {
            "name": "Pays",
            "cog": Millesime.M2024,
            "formatClass": Pays,
            "validTestCases": ["France", "Pays-Bas", "Bosnie-Herzégovine"],
            "invalidTestCases": ["L'Eldorado", "Zubrowska", "Pays Bas", "france"],
        },
        {
            "name": "NumeroDepartement",
            "cog": Millesime.M2023,
            "formatClass": NumeroDepartement,
            "validTestCases": ["05", "2B", "974"],
            "invalidTestCases": ["99", "051", "2b", "  97 4"],
        },
        {
            "name": "NumeroDepartement",
            "cog": Millesime.M2024,
            "formatClass": NumeroDepartement,
            "validTestCases": ["05", "2B", "974"],
            "invalidTestCases": ["99", "051", "2b", "  97 4"],
        },
    ]

    for tc in test_cases:
        validatorTest = ValidatorTest(
            tc["cog"], tc["validTestCases"], tc["invalidTestCases"], tc["formatClass"]
        )
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
