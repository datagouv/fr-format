from frformat import NumeroDepartement


def test_numero_departement():
    test_cases = ["05", "2B", "974"]
    for tc in test_cases:
        assert NumeroDepartement.is_valid(tc)
        assert NumeroDepartement.format(tc) == tc

    value = "99"
    assert not NumeroDepartement.is_valid(value)
