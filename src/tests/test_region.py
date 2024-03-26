from frformat import Region


def test_strict_region():
    valid_test_cases = ["Centre-Val de Loire", "La Réunion", "Corse"]
    for tc in valid_test_cases:
        assert Region.is_valid(tc)

    invalid_test_cases = ["Centre Val de Loire", "La Reunion", "corse"]
    for tc in invalid_test_cases:
        assert not Region.is_valid(tc)


def test_lenient_region():
    valid_test_cases = [
        "Centre-Val de Loire",
        "La Réunion",
        "Corse",
        "Centre Val de Loire",
        "La Reunion",
        "corse",
        "bfc",
        "aura",
    ]
    for tc in valid_test_cases:
        assert Region.is_valid(tc, strict=False)

    invalid_test_cases = ["Haute-Vienne", "Val-de-Marne"]
    for tc in invalid_test_cases:
        assert not Region.is_valid(tc)
