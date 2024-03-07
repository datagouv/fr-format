from frformat import CodeCommuneInsee


def test_code_commune_insee():
    value = "01015"
    assert CodeCommuneInsee.is_valid(value)
    assert CodeCommuneInsee.format(value) == value

    value = "2B002"
    assert CodeCommuneInsee.is_valid(value)

    value = "77777"
    assert not CodeCommuneInsee.is_valid(value)
