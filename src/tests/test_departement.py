from frformat import Departement


def test_departement():
    test_cases = ["05", "2B", "974"]
    for tc in test_cases:
        assert Departement.is_valid(tc)
        assert Departement.format(tc) == tc

    value = "99"
    assert not Departement.is_valid(value)
