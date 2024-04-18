import pytest

from frformat import Siren, Siret


def test_siret_format():
    siret = "83014132100034"
    expected_format = "830141321 00034"

    assert Siret.format(siret) == expected_format

    for siret in ["123", ""]:
        with pytest.raises(ValueError):
            Siret.format(siret)


def test_siren_format():
    siren = "830141321"
    expected_format = "830 141 321"
    assert Siren.format(siren) == expected_format
