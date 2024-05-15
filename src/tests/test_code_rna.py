from frformat import CodeRNA
from frformat.common import USPACE


def test_code_rna():
    value = "W135247934"
    assert CodeRNA.is_valid(value)
    assert CodeRNA.format(value) == "W135" + USPACE + "247" + USPACE + "934"

    assert CodeRNA.is_valid("W231468097")

    assert not CodeRNA.is_valid("w231468097")
    assert not CodeRNA.is_valid("W12754")
    assert not CodeRNA.is_valid("W667345")
    assert not CodeRNA.is_valid("a12754")
    assert not CodeRNA.is_valid("a231468097")
    assert not CodeRNA.is_valid("W23146809d")
    assert not CodeRNA.is_valid("W2314sj097")
    assert not CodeRNA.is_valid("W231468097z")
    assert not CodeRNA.is_valid("0")
