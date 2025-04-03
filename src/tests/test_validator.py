from frformat import Millesime, Validator


def test_validator():
    isvalid = Validator(Millesime.M2023).is_valid("01001")
    assert isvalid is True
