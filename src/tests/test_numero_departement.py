from frformat import NumeroDepartement
from tests.testing import validation_test_helper_factory

aux_test_numero_departement = validation_test_helper_factory(NumeroDepartement)


def test_numero_departement():
    test_cases = ["05", "2B", "974"]

    aux_test_numero_departement(test_cases, isStrict=True, expectValid=True)

    for tc in test_cases:
        assert NumeroDepartement.format(tc) == tc

    invalid_values = ["99", "2a", "2b"]
    aux_test_numero_departement(invalid_values, isStrict=True, expectValid=False)

    leniently_valid_values = ["2a", "2b"]
    aux_test_numero_departement(
        leniently_valid_values, isStrict=False, expectValid=True
    )
