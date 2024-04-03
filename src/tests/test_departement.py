from frformat import Departement
from tests.testing import validation_test_helper_factory

aux_test_departement = validation_test_helper_factory(Departement)


def test_strict_departement():
    valid_test_cases = ["Alpes-Maritimes", "Gard", "Mayotte", "Vendée"]
    aux_test_departement(valid_test_cases, isStrict=True, expectValid=True)

    invalid_test_cases = ["Alpes Maritimes", "gard", "Mayote", "Vendee"]
    aux_test_departement(invalid_test_cases, isStrict=True, expectValid=False)


def test_lenient_departement():
    valid_test_cases = [
        "Alpes-Maritimes",
        "Gard",
        "Mayotte",
        "Vendée",
        "Alpes Maritimes",
        "gard",
        "Vendee",
    ]
    aux_test_departement(valid_test_cases, isStrict=False, expectValid=True)

    invalid_test_cases = ["Mayote"]
    aux_test_departement(invalid_test_cases, isStrict=False, expectValid=False)
