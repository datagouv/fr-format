import csv
import io
import os
import urllib.parse
import urllib.request


def _get_valid_values_from_remote_csv(path: str) -> io.StringIO:
    try:
        response = urllib.request.urlopen(path)
        csvfile = io.StringIO(response.read().decode("utf-8"))
    except Exception as e:
        raise ValueError(f"Failed to fetch CSV from URL: {e} .")

    return csvfile


def _get_valid_values_from_local_csv(path: str) -> io.TextIOWrapper:
    try:
        csvfile = open(path, newline="", encoding="utf-8")

    except Exception as e:
        raise ValueError(f"Failed to open local CSV file: {e} .")

    return csvfile


def get_valid_values_from_csv(path: str, column: str) -> frozenset[str]:

    valid_values = []

    parsed_uri = urllib.parse.urlparse(path)
    is_remote = parsed_uri.scheme in ("http", "https")

    if is_remote:
        csvfile = _get_valid_values_from_remote_csv(path)

    elif os.path.isfile(path):
        csvfile = _get_valid_values_from_local_csv(path)

    else:
        raise ValueError(f"Invalid path: {path}.It must be a URL or existing csv file.")

    with csvfile:
        try:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if column in row:
                    valid_values.append(row[column])
                else:
                    raise ValueError(f"CSV file is missing the {column} column.")
        except UnicodeDecodeError as e:
            print(f"Failed to convert the csv file to python dictionnary: {e}")
            raise e

    return frozenset(valid_values)
