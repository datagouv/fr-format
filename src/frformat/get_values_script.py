import csv
import io
import os
import time
import urllib.parse
import urllib.request


def get_valid_values(path: str, column: str) -> frozenset[str]:

    parsed_url = urllib.parse.urlparse(path)
    is_url = parsed_url.scheme in ("http", "https")

    valid_values = []

    if is_url:
        try:
            response = urllib.request.urlopen(path)
            time.sleep(1)
            csvfile = io.StringIO(response.read().decode("utf-8"))
        except Exception as e:
            raise ValueError(f"Failed to fetch CSV from URL: {e} .")

    elif os.path.isfile(path):
        splitted_path = path.split(".")
        if splitted_path[len(splitted_path) - 1] == "csv":
            try:
                csvfile = open(path, newline="", encoding="utf-8")

            except Exception as e:
                raise ValueError(f"Failed to open local CSV file: {e} .")
        else:
            raise ValueError("The given path must be referenced to a csv file.")
    else:
        raise ValueError(f"Invalid path: {path}.It must be a URL or existing csv file.")

    with csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if column in row:
                valid_values.append(row[column])
            else:
                raise ValueError(f"CSV file is missing the {column} column.")

    return frozenset(valid_values)
