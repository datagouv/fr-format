import pytest

from frformat import Millesime, Validator
from frformat.get_values_script import get_valid_values_from_csv


def test_validator():
    isvalid = Validator(Millesime.M2023).is_valid("booker12")
    assert isvalid is True


def test_get_valid_values_with_local_file():
    valid_values = get_valid_values_from_csv(
        "src/tests/test_files_data/values.csv", "First name"
    )
    assert valid_values == frozenset({"Rachel", "Laura"})

    with pytest.raises(UnicodeError):
        valid_values = get_valid_values_from_csv(
            "src/tests/test_files_data/text_file.odt", "coucou"
        )

    """ with pytest.raises(ValueError, match="CSV file is missing the Link column."):
        valid_values = get_valid_values_from_csv(
            "src/tests/test_files_data/values.csv", "Link"
        )

    with pytest.raises(ValueError):
        valid_values = get_valid_values_from_csv(
            "src/tests/test_files_data/non_existed_file.csv", "DEP"
        ) """


# mocking ?
""" def test_get_valid_values_with_url():
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

    with pytest.raises(ValueError):
        valid_values = get_valid_values(
            "https://coucou.csv/",
            "Name",
        )
 """
