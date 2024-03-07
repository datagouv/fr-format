from frformat import PostalCode


def test_postal_code():
    value = "05560"
    assert PostalCode.is_valid(value)
