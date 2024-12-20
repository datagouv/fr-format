from frformat import CodeRNA
from frformat.common import NNBSP


def test_code_rna():
    value = "W135247934"
    code_rna = CodeRNA()
    assert code_rna.is_valid(value)
    assert code_rna.format(value) == "W135" + NNBSP + "247" + NNBSP + "934"

    assert code_rna.is_valid("W231468097")

    invalid_test_cases = [
        "w231468097",
        "W  135247934 ",
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
        assert not code_rna.is_valid(tc)
