from frformat import PostalCode


def test_postal_code():
    value = "05560"
    assert PostalCode.is_valid(value)

    value = "77777"
    assert not PostalCode.is_valid(value)
