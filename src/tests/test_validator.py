import pytest

from frformat import Millesime, Validator
from frformat.get_values_script import get_valid_values


def test_validator():
    isvalid = Validator(Millesime.M2023).is_valid("01001")
    assert isvalid is True


def test_get_valid_values_with_local_file():
    valid_values = get_valid_values(
        "src/tests/test_files_data/values.csv", "First name"
    )
    assert valid_values == frozenset({"Rachel", "Laura"})

    with pytest.raises(ValueError, match="CSV file is missing the Link column."):
        valid_values = get_valid_values("src/tests/test_files_data/values.csv", "Link")


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

    with pytest.raises(
        ValueError, match="Failed to fetch CSV from URL: HTTP Error 403: Forbidden ."
    ):
        valid_values = get_valid_values(
            "https://cd.wsform.com/wp-content/uploads/2021/04/month.csv",
            "Name",
        )
