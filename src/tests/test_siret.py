import pytest

from frformat import Siret


def test_siret_format():
    siret = "83014132100034"
    expected_format = "830141321 00034"

    assert Siret.format(siret) == expected_format

    for siret in ["123", ""]:
        with pytest.raises(ValueError):
            Siret.format(siret)
