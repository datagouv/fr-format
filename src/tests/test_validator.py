from frformat import Millesime, Validator
from frformat.get_values_script import get_valid_values


def test_validator():
    isvalid = Validator(Millesime.M2023).is_valid("01001")
    assert isvalid is True


def test_get_valid_values_with_local_file():
    valid_values = get_valid_values("src/frformat/formats/values.csv", "First name")
    assert valid_values == frozenset({"Rachel", "Laura"})


def test_get_valid_values_with_url():
    valid_values = get_valid_values(
        "https://cdn.wsform.com/wp-content/uploads/2021/04/month.csv",
        "Name",
    )
    assert valid_values == frozenset(
        {
            "January",
            "Feburary",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        }
    )
