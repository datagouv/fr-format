from frformat import CodeFantoir, CodePostal, LatitudeL93, LongitudeL93
from frformat.common import NBSP, NNBSP


def test_code_fantoir():
    fantoir_valid = "ZB03A"
    fantoir_invalid = ["1000", "zB03A"]

    code_fantoir = CodeFantoir()
    assert code_fantoir.is_valid(fantoir_valid)
    for fi in fantoir_invalid:
        assert not code_fantoir.is_valid(fi)


def test_code_postal():
    value = "05560"
    code_postal = CodePostal()
    assert code_postal.is_valid(value)
    assert code_postal.format(value) == value
    codes_postales_invalides = ["77777", "2B002"]
    for cpi in codes_postales_invalides:
        assert not code_postal.is_valid(cpi)


def test_longitude_l93():
    longitudel93 = LongitudeL93()
    assert longitudel93.format(224234) == "224" + NNBSP + "234" + NBSP + "m"
    assert longitudel93.format(224234.0) == "224" + NNBSP + "234,00" + NBSP + "m"

    invalid_test_cases = [-435522.3, -554234, 2076524, 5436780.23]

    for tc in invalid_test_cases:
        assert not longitudel93.is_valid(tc)

    valid_test_cases = [0, 1234546, 1234546.32, -123554, -234.546]

    for tc in valid_test_cases:
        assert longitudel93.is_valid(tc)


def test_latitude_l93():
    latitudel93 = LatitudeL93()
    assert (
        latitudel93.format(6757121) == "6" + NNBSP + "757" + NNBSP + "121" + NBSP + "m"
    )
    assert (
        latitudel93.format(6757121.337)
        == "6" + NNBSP + "757" + NNBSP + "121,34" + NBSP + "m"
    )

    assert latitudel93.is_valid(6544234.2)
    assert latitudel93.is_valid(7145278)

    invalid_test_cases = [0, -6145765.9, -7234567, 7233478, 6000658.5]

    for tc in invalid_test_cases:
        assert not latitudel93.is_valid(tc)
