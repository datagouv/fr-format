import csv
import io
import os
import urllib.parse
import urllib.request


def _get_values_from_remote_csv(path: str) -> io.StringIO:
    try:
        response: urllib.request._UrlopenRet = urllib.request.urlopen(path)
        csvfile: io.StringIO = io.StringIO(response.read().decode("utf-8"))
        return csvfile
    except Exception as e:
        raise Exception(f"An error is occured: {e}")


def _get_values_from_local_csv(path: str) -> io.TextIOWrapper:
    try:
        csvfile: io.TextIOWrapper = open(path, newline="", encoding="utf-8")
        return csvfile
    except Exception as e:
        raise Exception(f"An error is occured: {e}")


def get_values_from_csv(path: str, column: str) -> frozenset[str]:
    """
    Extract all values from a given column in a well-formatted CSV file
    located either locally or remotely.

    Supported sources:
    - Local files without a URI scheme.
    - Remote files using 'http', 'https', 'file' schemes.
    - Unsupported scheme: 'ftp' is not allowed.

    Args:
        path (string type): The path or URL to the CSV file.
        column (string type): The name of the column from which to extract values.

    Raises:
        ValueError: If the file is missing, the column is not found, or the path uses
                    an unsupported scheme.
        UnicodeError: If the file cannot be parsed as a valid CSV.

    Returns:
        frozenset[str]: A frozenset containing the values found in the specified column.
    """

    try:
        values: list[str] = []

        parsed_uri: urllib.parse.ParseResult = urllib.parse.urlparse(path)
        is_remote: bool = parsed_uri.scheme in ("http", "https", "file")

        if not is_remote and not os.path.isfile(path):
            raise ValueError(
                f"Invalid path: {path}.The URI must use one of the following schemes: http, https, or file or it must be existing csv file."
            )

        if is_remote:
            csvfile = _get_values_from_remote_csv(path)

        else:
            csvfile = _get_values_from_local_csv(path)

        with csvfile:
            reader: csv.DictReader[str] = csv.DictReader(csvfile)
            try:
                for row in reader:
                    if column in row:
                        values.append(row[column])
                    else:
                        raise ValueError(f"CSV file is missing the {column} column.")
            except UnicodeError as e:
                raise UnicodeError(f"The file is not well csv formatted: {e}")

        return frozenset(values)
    except Exception as e:
        print(f"An error is occured where getting values from csv: {e}")
        raise
