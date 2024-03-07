from frformat import InseeCityCode


def test_insee_cty_code():
    value = "01015"
    assert InseeCityCode.is_valid(value)
    assert InseeCityCode.format(value) == value

    value = "2B002"
    assert InseeCityCode.is_valid(value)

    value = "77777"
    assert not InseeCityCode.is_valid(value)
