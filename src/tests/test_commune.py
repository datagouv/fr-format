from frformat import Commune

communes_random = ["Bellac", "Le Dorat", "Petite-Île", "L'Isle-Adam"]


def test_strict_commune():
    valid_test_cases = communes_random
    for tc in valid_test_cases:
        assert Commune.is_valid(tc)

    invalid_test_cases = [
        "bellac",
        "le Dorat",
        "Petite-Ile",
        "L'Isle Adam",
        "commune inexistante",
    ]
    for tc in invalid_test_cases:
        assert not Commune.is_valid(tc)


def test_lenient_commune():
    valid_test_cases = communes_random + [
        "bellac",
        "le Dorat",
        "Petite-Ile",
        "l isle adam",
    ]
    for tc in valid_test_cases:
        assert Commune.is_valid(tc, strict=False)

    invalid_test_cases = ["commune inexistante"]
    for tc in invalid_test_cases:
        assert not Commune.is_valid(tc)
