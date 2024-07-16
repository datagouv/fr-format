import pytest

from frformat import Siren, Siret
from frformat.common import NNBSP


def test_siret_format():
    siret_example = "83014132100034"
    expected_format = f"830141321{ NNBSP }00034"

    siret = Siret()
    assert siret.format(siret_example) == expected_format

    for siret_value in ["123", ""]:
        with pytest.raises(ValueError):
            siret.format(siret_value)


def test_siren_format():
    siren_example = "830141321"
    expected_format = f"830{ NNBSP }141{ NNBSP }321"
    siren = Siren()
    assert siren.format(siren_example) == expected_format
