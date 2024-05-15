from frformat import CodeRNA
from frformat.common import USPACE


def test_code_rna():
    value = "W135247934"
    assert CodeRNA.is_valid(value)
    assert CodeRNA.format(value) == "W135" + USPACE + "247" + USPACE + "934"

    assert CodeRNA.is_valid("W231468097")

    invalid_test_cases = [
        "w231468097",
        "W12754",
        "W667345",
        "a12754",
        "a231468097",
        "W23146809d",
        "W2314sj097",
        "W231468097z",
        "0",
    ]

    for tc in invalid_test_cases:
        assert not CodeRNA.is_valid(tc)
