import csv
import io
import os
import urllib.parse
from typing import Protocol, Union


class IFileReader(Protocol):

    def read_file(self, path: str) -> Union[io.StringIO, io.TextIOWrapper]: ...


def get_values_from_csv(
    path: str, column: str, remote_reader: IFileReader, local_reader: IFileReader
) -> frozenset[str]:
    """
    Extract all values from a given column in a well-formatted CSV file
    located either locally or remotely.

    Supported sources:
    - Local files and file with 'file' scheme.
    - Remote files using 'http'and 'https' schemes.

    Args:
        path: The path or URL to the CSV file.
        column: The name of the column from which to extract values.

    Raises:
        ValueError: If the file is missing, the column is not found, the path uses
                    an unsupported scheme or the file cannot be parsed as a valid CSV.

    Returns:
        A frozenset containing the values found in the specified column.
    """

    try:
        values: list[str] = []

        parsed_uri: urllib.parse.ParseResult = urllib.parse.urlparse(path)
        is_valid_scheme: bool = parsed_uri.scheme in ("http", "https", "file")

        if not is_valid_scheme and not os.path.isfile(path):
            raise ValueError(
                f"Invalid path: {path}.The URI must use one of the following schemes: http, https, or file or it must be existing csv file."
            )

        if is_valid_scheme:
            csvfile = remote_reader.read_file(path)

        else:
            csvfile = local_reader.read_file(path)

        with csvfile:
            reader: csv.DictReader[str] = csv.DictReader(csvfile)
            try:
                for row in reader:
                    if column in row:
                        values.append(row[column])
                    else:
                        raise ValueError(f"CSV file is missing the {column} column.")
            except ValueError as e:
                raise ValueError(f"The file is not well csv formatted: {e}")

        return frozenset(values)
    except Exception as e:
        print(f"An error is occured where getting values from csv: {e}")
        raise
