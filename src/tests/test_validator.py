import pytest

from frformat import Millesime, Validator
from frformat.get_values import get_values_from_csv
from frformat.infra_file_reader import LocalReader, RemoteReader


def test_validator():
    isvalid = Validator(Millesime.M2023).is_valid("booker12")
    assert isvalid is True


local_reader = LocalReader()
remote_reader = RemoteReader()


def test_get_valid_values_with_local_file():
    valid_values = get_values_from_csv(
        "src/tests/test_files_data/values.csv",
        "First name",
        remote_reader,
        local_reader,
    )
    assert valid_values == frozenset({"Rachel", "Laura"})

    with pytest.raises(UnicodeError):
        get_values_from_csv(
            "src/tests/test_files_data/not_formatted_file.csv",
            "coucou",
            remote_reader,
            local_reader,
        )

    with pytest.raises(ValueError):
        get_values_from_csv(
            "src/tests/test_files_data/values.csv", "Link", remote_reader, local_reader
        )

    with pytest.raises(ValueError):
        get_values_from_csv(
            "src/tests/test_files_data/non_existed_file.csv",
            "DEP",
            remote_reader,
            local_reader,
        )


# Dependency inversion remote paths
""" def test_get_valid_values_with_remote_csv():

    valid_values = get_values_from_csv(
        "https://cdn.wsform.com/wp-content/uploads/2021/04/month.csv",
        "Name",
        remote_reader,
        local_reader,
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
        valid_values = get_values_from_csv(
            "https://coucou.csv/",
            "Name",
            remote_reader,
            local_reader,
        )

    valid_values = get_values_from_csv(
        "file:///home/sarraba/multi/multi_projects_inter/fr-format/src/tests/test_files_data/values.csv",
        "First name",
        remote_reader,
        local_reader,
    )
    assert valid_values == frozenset({"Rachel", "Laura"})

    with pytest.raises(ValueError):
        get_values_from_csv(
            "ftp:///home/sarraba/multi/multi_projects_inter/fr-format/src/tests/test_files_data/values.csv",
            "First name",
            remote_reader,
            local_reader,
        ) """
