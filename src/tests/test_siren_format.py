from frformat import Siren


def test_siren_format():
    siren = "830141321"
    expected_format = "830 141 321"
    assert Siren.format(siren) == expected_format
