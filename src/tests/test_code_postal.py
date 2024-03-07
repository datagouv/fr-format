from frformat import CodePostal


def test_code_postal():
    value = "05560"
    assert CodePostal.is_valid(value)
    assert CodePostal.format(value) == value

    value = "77777"
    assert not CodePostal.is_valid(value)
