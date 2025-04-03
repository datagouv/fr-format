import csv
import io
import os
import urllib.parse
import urllib.request


def get_valid_values(path: str, column: str) -> frozenset:

    parsed_url = urllib.parse.urlparse(path)
    is_url = parsed_url.scheme in ("http", "https")

    valid_values = []

    if is_url:
        try:
            response = urllib.request.urlopen(path)
            csvfile = io.StringIO(response.read().decode("utf-8"))
        except Exception as e:
            raise ValueError(f"Failed to fetch CSV from URL: {e}")

    elif os.path.isfile(path):
        try:
            csvfile = open(path, newline="", encoding="utf-8")
        except Exception as e:
            raise ValueError(f"Failed to open local CSV file: {e}")

    else:
        raise ValueError(f"Invalid path: {path}. Must be a URL or existing file.")

    with csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if column in row:
                valid_values.append(row[column])
            else:
                raise ValueError("CSV file is missing the {column} column.")

    return frozenset(valid_values)
