from typing import List

from frformat import Departement


def aux_test_departement(
    test_cases: List[str], isStrict: bool, expectValid: bool
) -> None:
    adjective = "strictly" if isStrict else "leniently"
    validKeywoard = "valid" if expectValid else "invalid"

    for tc in test_cases:
        assert (
            Departement.is_valid(tc, strict=isStrict) == expectValid
        ), f"Check that departement { tc } is { adjective } { validKeywoard }"


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
