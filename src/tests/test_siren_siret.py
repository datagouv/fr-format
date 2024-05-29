import pytest

from frformat import Siren, Siret
from frformat.common import NNBSP


def test_siret_format():
    siret = "83014132100034"
    expected_format = f"830141321{ NNBSP }00034"

    assert Siret.format(siret) == expected_format

    for siret in ["123", ""]:
        with pytest.raises(ValueError):
            Siret.format(siret)


def test_siren_format():
    siren = "830141321"
    expected_format = f"830{ NNBSP }141{ NNBSP }321"
    assert Siren.format(siren) == expected_format
