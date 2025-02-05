from frformat import (
    Canton,
    CodeCommuneInsee,
    CodeFantoir,
    CodePaysISO2,
    CodePaysISO3,
    CodePostal,
    CodeRegion,
    Commune,
    Departement,
    LatitudeL93,
    LongitudeL93,
    Millesime,
    NumeroDepartement,
    Pays,
    Region,
    set_format,
)
from frformat.common import NBSP, NNBSP
from frformat.versioned_set import VersionedSet


class TestInseeGeoFormat:
    class ValidatorTest:
        """
        This class tests all INSEE geographical formats, versioned by the Millesime enum.

        The __init__ function takes a cog parameter for the version,
        which refers to the "Code officiel géographique" (Official Geographical Code).
        """

        def __init__(self, cog, validTestCases, invalidTestCases, formatClass):
            self.cog = cog
            self.validTestCases = validTestCases
            self.invalidTestCases = invalidTestCases
            self.formatClass = formatClass

        def test_valid_cases(self):
            for tc in self.validTestCases:
                assert self.formatClass(self.cog).is_valid(
                    tc
                ), f"Check that {tc} is not valid when the class format is {self.formatClass} and the cog is equal to {self.cog}"

        def test_invalid_cases(self):
            for tc in self.invalidTestCases:
                assert not self.formatClass(self.cog).is_valid(
                    tc
                ), f"Check that {tc} is valid when the class format is {self.formatClass} and the cog is equal to {self.cog}."

        def run_all_tests(self):
            self.test_valid_cases()
            self.test_invalid_cases()

    def test_all_fomats_validation(self):
        test_cases = [
            {
                "name": "code_region_millesime2023",
                "cog": Millesime.M2023,
                "formatClass": CodeRegion,
                "validTestCases": ["01", "75"],
                "invalidTestCases": ["AA", "00", "7 5"],
            },
            {
                "name": "code_region_millesime2024",
                "cog": Millesime.M2024,
                "formatClass": CodeRegion,
                "validTestCases": ["01", "75"],
                "invalidTestCases": ["AA", "00", "7 5"],
            },
            {
                "name": "region_millesime2023",
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
                "name": "region_millesime2024",
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
                "name": "commune_millesime2023",
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
                "name": "commune_millesime2024",
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
                "name": "canton_millesime2023",
                "cog": Millesime.M2023,
                "formatClass": Canton,
                "validTestCases": [
                    "Lagnieu",
                    "Meximieux",
                ],
                "invalidTestCases": ["Paris", "Lyon", "paris"],
            },
            {
                "name": "canton_millesime2024",
                "cog": Millesime.M2024,
                "formatClass": Canton,
                "validTestCases": ["Paris", "Lyon"],
                "invalidTestCases": ["Saint Quentin", "saint  quentin"],
            },
            {
                "name": "code_paysISO2_millesime2023",
                "cog": Millesime.M2023,
                "formatClass": CodePaysISO2,
                "validTestCases": ["BV", "SJ"],
                "invalidTestCases": ["RWA", "TCD", "rwa"],
            },
            {
                "name": "code_paysISO2_millesime2024",
                "cog": Millesime.M2024,
                "formatClass": CodePaysISO2,
                "validTestCases": ["FR", "JP"],
                "invalidTestCases": ["BV", "SJ", "bv"],
            },
            {
                "name": "code_paysISO3_millesime2023",
                "cog": Millesime.M2023,
                "formatClass": CodePaysISO3,
                "validTestCases": ["BVT", "SJM"],
                "invalidTestCases": ["BF", "GH", "gh"],
            },
            {
                "name": "code_paysISO3_millesime2024",
                "cog": Millesime.M2024,
                "formatClass": CodePaysISO3,
                "validTestCases": ["FRA", "JPN"],
                "invalidTestCases": ["BVT", "SJM", "bvt"],
            },
            {
                "name": "departement_millesime2023",
                "cog": Millesime.M2023,
                "formatClass": Departement,
                "validTestCases": ["Alpes-Maritimes", "Gard", "Mayotte", "Vendée"],
                "invalidTestCases": [
                    "Charente-Inférieure",
                    "Vendee",
                    "Alpes  maritimes",
                ],
            },
            {
                "name": "departement_millesime2024",
                "cog": Millesime.M2024,
                "formatClass": Departement,
                "validTestCases": ["Alpes-Maritimes", "Gard", "Mayotte", "Vendée"],
                "invalidTestCases": [
                    "Charente-Inférieure",
                    "Vendee",
                    "Alpes  maritimes",
                ],
            },
            {
                "name": "pays_millesime2024",
                "cog": Millesime.M2024,
                "formatClass": Pays,
                "validTestCases": ["France", "Pays-Bas", "Bosnie-Herzégovine"],
                "invalidTestCases": ["L'Eldorado", "Zubrowska", "Pays Bas", "france"],
            },
            {
                "name": "numero_departement_millesime2023",
                "cog": Millesime.M2023,
                "formatClass": NumeroDepartement,
                "validTestCases": ["05", "2B", "974"],
                "invalidTestCases": ["99", "051", "2b", "  97 4"],
            },
            {
                "name": "numero_departement_millesime2024",
                "cog": Millesime.M2024,
                "formatClass": NumeroDepartement,
                "validTestCases": ["05", "2B", "974"],
                "invalidTestCases": ["99", "051", "2b", "  97 4"],
            },
            {
                "name": "code_commune_insee__millesime2023",
                "cog": Millesime.M2023,
                "formatClass": CodeCommuneInsee,
                "validTestCases": ["01015", "2B002"],
                "invalidTestCases": ["77777", "  01015"],
            },
            {
                "name": "code_commune_insee_millesime2024",
                "cog": Millesime.M2024,
                "formatClass": CodeCommuneInsee,
                "validTestCases": ["64300", "2A331"],
                "invalidTestCases": ["64402", "64  300"],
            },
        ]

        for tc in test_cases:
            validatorTest = self.ValidatorTest(
                tc["cog"],
                tc["validTestCases"],
                tc["invalidTestCases"],
                tc["formatClass"],
            )
            validatorTest.run_all_tests()

    def test_code_commune_insee_format(self):
        code_commune_insee_cog_2023 = CodeCommuneInsee(Millesime.M2023)
        code_commune_insee_cog_2024 = CodeCommuneInsee(Millesime.M2024)

        cog_2023_value = "01015"
        assert code_commune_insee_cog_2023.format(cog_2023_value) == cog_2023_value

        cog_2024_value = "64300"

        assert code_commune_insee_cog_2024.format(cog_2024_value) == cog_2024_value

    def test_formats_valid_values(self):
        versioned_data = VersionedSet[Millesime]()
        versioned_data.add_version(
            Millesime.M2024, frozenset({"Paris", "Lyon"})
        )
        test_cases = [
            {
                "valid_data": versioned_data,
                "version": "2024",
                "expected_result": frozenset({"Paris", "Lyon"}),
            },
            {
                "valid_data": frozenset({"Nomandie", "Nice"}),
                "version": None,
                "expected_result": frozenset({"Nomandie", "Nice"}),
            },
        ]

        name = "Validator name"
        description = "Validator description"

        for tc in test_cases:
            validator = set_format.new("Validator", name, description, tc["valid_data"])
            if tc["version"]:
                assert (
                    validator(tc["version"]).get_valid_values_set()
                    == tc["expected_result"]
                ), f"The returned data is not equal to {tc['expected_result']} when the valid_data is {tc['valid_data']} and the version is equal to {tc['version']}"
            else:
                assert (
                    validator().get_valid_values_set() == tc["expected_result"]
                ), f"The returned data is not equal to {tc['expected_result']} when the valid_data is {tc['valid_data']} and the version is equal to {tc['version']}"


class TestGeoFormat:
    """This method tests geographical formats, which does not belong to the Official Geographic Code."""

    def test_code_fantoir(self):
        fantoir_valid = "ZB03A"
        fantoir_invalid = ["1000", "zB03A"]

        code_fantoir = CodeFantoir()
        assert code_fantoir.is_valid(fantoir_valid)
        for fi in fantoir_invalid:
            assert not code_fantoir.is_valid(fi)

    def test_code_postal(self):
        value = "05560"
        code_postal = CodePostal()
        assert code_postal.is_valid(value)
        assert code_postal.format(value) == value
        codes_postales_invalides = ["77777", "2B002"]
        for cpi in codes_postales_invalides:
            assert not code_postal.is_valid(cpi)

    def test_longitude_l93(self):
        longitudel93 = LongitudeL93()
        assert longitudel93.format(224234) == "224" + NNBSP + "234" + NBSP + "m"
        assert longitudel93.format(224234.0) == "224" + NNBSP + "234,00" + NBSP + "m"

        invalid_test_cases = [-435522.3, -554234, 2076524, 5436780.23]

        for tc in invalid_test_cases:
            assert not longitudel93.is_valid(tc)

        valid_test_cases = [0, 1234546, 1234546.32, -123554, -234.546]

        for tc in valid_test_cases:
            assert longitudel93.is_valid(tc)

    def test_latitude_l93(self):
        latitudel93 = LatitudeL93()
        assert (
            latitudel93.format(6757121)
            == "6" + NNBSP + "757" + NNBSP + "121" + NBSP + "m"
        )
        assert (
            latitudel93.format(6757121.337)
            == "6" + NNBSP + "757" + NNBSP + "121,34" + NBSP + "m"
        )

        assert latitudel93.is_valid(6544234.2)
        assert latitudel93.is_valid(7145278)

        invalid_test_cases = [0, -6145765.9, -7234567, 7233478, 6000658.5]

        for tc in invalid_test_cases:
            assert not latitudel93.is_valid(tc)
