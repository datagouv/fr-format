from io import StringIO, TextIOBase

import pytest

from frformat import Millesime, Validator
from frformat.get_values import IFileReader, get_values_from_csv
from frformat.infra_file_reader import LocalReader, RemoteReader


def test_validator():
    isvalid = Validator(Millesime.M2023).is_valid("booker12")
    assert isvalid is True


class FakeFileReader(IFileReader):
    def __init__(self, data: str):
        self._data = data

    def read_file(self, path: str) -> TextIOBase:
        return StringIO(self._data)


def test_get_values_from_local_file():

    csv_data: str = (
        "Username,Email\nbooker1,booker12@example.com\ngrey7,grey07@example.com"
    )

    local_reader = FakeFileReader(csv_data)

    remote_reader = RemoteReader()

    valid_values = get_values_from_csv(
        "src/tests/test_files_data/values.csv",
        "Username",
        remote_reader,
        local_reader,
    )

    assert valid_values == frozenset({"booker1", "grey7"})

    values = get_values_from_csv(
        "src/tests/test_files_data/values.csv", "Link", remote_reader, local_reader
    )
    assert values == frozenset({})


def test_get_values_from_not_well_formatted_local_file():
    csv_data: str = "xff�Name,Age\nJohn,30"

    local_reader = FakeFileReader(csv_data)

    remote_reader = RemoteReader()
    values = get_values_from_csv(
        "src/tests/test_files_data/values.csv",
        "coucou",
        remote_reader,
        local_reader,
    )
    assert values == frozenset({})


def test_invalid_path_file():
    remote_reader = RemoteReader()
    local_reader = LocalReader()

    with pytest.raises(
        ValueError,
        match="Invalid path: src/tests/test_files_data/non_existed_file.csv.The URI must use one of the following schemes: http, https, or file or it must be existing csv file.",
    ):
        get_values_from_csv(
            "src/tests/test_files_data/non_existed_file.csv",
            "DEP",
            remote_reader,
            local_reader,
        )


def test_get_values_from_remote_csv():
    csv_data: str = "Age,RegionCode\n23,7653\n22,5498"

    remote_reader = FakeFileReader(csv_data)

    local_reader = LocalReader()

    valid_values = get_values_from_csv(
        "https://some.fake.url/values.csv",
        "Age",
        remote_reader,
        local_reader,
    )

    assert valid_values == frozenset({"23", "22"})

    valid_values = get_values_from_csv(
        "https://some.fake.url/values.csv",
        "Name",
        remote_reader,
        local_reader,
    )

    assert valid_values == frozenset({})

    valid_values = get_values_from_csv(
        "file:///fakedata/values.csv",
        "RegionCode",
        remote_reader,
        local_reader,
    )
    assert valid_values == frozenset({"7653", "5498"})
