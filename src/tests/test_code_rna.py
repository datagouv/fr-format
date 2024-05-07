from frformat import CodeRNA


def test_code_rna():
    value = "W135247934"
    assert CodeRNA.is_valid(value)
    assert CodeRNA.format(value) == value

    assert CodeRNA.is_valid("w231468097")
    assert not CodeRNA.is_valid("w12754")
    assert not CodeRNA.is_valid("W667345")
    assert not CodeRNA.is_valid("a12754")
    assert not CodeRNA.is_valid("a231468097")
    assert not CodeRNA.is_valid("w23146809d")
    assert not CodeRNA.is_valid("w2314sj097")
    assert not CodeRNA.is_valid("w231468097z")
    assert not CodeRNA.is_valid("0")
