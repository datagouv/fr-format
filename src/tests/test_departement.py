from frformat import Departement


def test_strict_departement():
    valid_test_cases = ["Alpes-Maritimes", "Gard", "Mayotte", "Vendée"]
    for tc in valid_test_cases:
        assert Departement.is_valid(tc), f"Check that departement { tc } is valid"

    invalid_test_cases = ["Alpes Maritimes", "gard", "Mayote", "Vendee"]
    for tc in invalid_test_cases:
        assert not Departement.is_valid(tc), f"Check that departement { tc } is invalid"


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
    for tc in valid_test_cases:
        assert Departement.is_valid(tc, strict=False)

    invalid_test_cases = ["Mayote"]
    for tc in invalid_test_cases:
        assert not Departement.is_valid(tc, strict=False)
