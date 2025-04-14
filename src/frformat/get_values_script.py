import csv
import io
import os
import urllib.parse
import urllib.request


def _get_valid_values_from_remote_csv(path: str) -> io.StringIO:
    response = urllib.request.urlopen(path)
    csvfile = io.StringIO(response.read().decode("utf-8"))
    return csvfile


def _get_valid_values_from_local_csv(path: str) -> io.TextIOWrapper:
    csvfile = open(path, newline="", encoding="utf-8")
    print(csvfile)
    return csvfile


def get_valid_values_from_csv(path: str, column: str) -> frozenset[str]:

    valid_values = []

    parsed_uri = urllib.parse.urlparse(path)
    is_remote = parsed_uri.scheme in ("http", "https")

    if not is_remote and not os.path.isfile(path):
        raise ValueError(f"Invalid path: {path}.It must be a URL or existing csv file.")

    if is_remote:
        csvfile = _get_valid_values_from_remote_csv(path)

    else:
        csvfile = _get_valid_values_from_local_csv(path)

    with csvfile:
        reader = csv.DictReader(csvfile)
        ## error when it isn't a csv well formatted
        try:
            for row in reader:
                if column in row:
                    valid_values.append(row[column])
                else:
                    raise ValueError(f"CSV file is missing the {column} column.")
        except UnicodeError as e:
            print(e.__class__.__name__)
            raise UnicodeError(f"the csv file is not well formatted: {e}")

    return frozenset(valid_values)
