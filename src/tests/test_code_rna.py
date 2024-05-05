from frformat import CodeRna


def test_code_rna():
    value = "W135247934"
    assert CodeRna.is_valid(value)
    assert CodeRna.format(value) == value

    assert CodeRna.is_valid("w231468097")
    assert not CodeRna.is_valid("w12754")
    assert not CodeRna.is_valid("W667345")
    assert not CodeRna.is_valid("a12754")
    assert not CodeRna.is_valid("a231468097")
    assert not CodeRna.is_valid("w23146809d")
    assert not CodeRna.is_valid("w2314sj097")
    assert not CodeRna.is_valid("w231468097z")
    assert not CodeRna.is_valid("0")
