from frformat import Pays
from tests.testing import validation_test_helper_factory

aux_test_pays = validation_test_helper_factory(Pays)


def test_pays():
    pays_strict = ["France", "Pays-Bas", "Bosnie-Herzégovine"]
    pays_lenient = ["france", "Pays Bas", "bosnie herzegovine"]
    pays_nonexistant = ["Zubrowska"]

    aux_test_pays(test_cases=pays_strict, isStrict=True, expectValid=True)
    aux_test_pays(test_cases=pays_lenient, isStrict=True, expectValid=False)
    aux_test_pays(test_cases=pays_nonexistant, isStrict=True, expectValid=False)

    aux_test_pays(test_cases=pays_strict, isStrict=False, expectValid=True)
    aux_test_pays(test_cases=pays_lenient, isStrict=False, expectValid=True)
    aux_test_pays(test_cases=pays_nonexistant, isStrict=False, expectValid=False)
