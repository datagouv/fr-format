"""
A set format is a format that validates if a value is within a given set of
valid values.

This module introduces utilities to efficiently create new set formats :

- GenericSetFormat creates a validator with valid data passed on the fly
- `new` creates specialized versions where data is tied to the class
"""

import csv
import io
import logging
import os
import urllib.parse
from typing import (
    ClassVar,
    FrozenSet,
    Generic,
    Protocol,
    Type,
    TypeVar,
    Union,
    overload,
)

from frformat import CustomStrFormat, Metadata
from frformat.common import normalize_value
from frformat.infra_file_reader import LocalReader, RemoteReader
from frformat.options import Options
from frformat.versioned_set import Version, VersionedSet


class IFileReader(Protocol):
    def read_file(self, path: str) -> io.TextIOBase: ...


class SingleSetFormat(CustomStrFormat):
    """This format defines a closed list of valid values"""

    _valid_values: FrozenSet = frozenset()
    """Dataset of valid values.

       Technical details:

       Beware, child classes may define an instance `_valid_values` attribute, which
       will always take precedence over the class attribute for the validation.
    """
    remote_reader: ClassVar[IFileReader] = RemoteReader()
    """ RemoteReader is a class that contain a method to read file with remote path"""

    local_reader: ClassVar[IFileReader] = LocalReader()
    """ LocalReader is a class that contain a method to read file with local path"""

    def __init__(self, options: Options = Options()):
        self._options = options

        normalized_extra_values = {
            normalize_value(e, self._options) for e in self._options.extra_valid_values
        }

        self._normalized_values = {
            normalize_value(e, self._options)
            for e in self._valid_values
            # in child classes, `self._valid_values` can reference an instance
            # attribute, if applicable ; otherwise the class attribute will
            # be used
        }.union(normalized_extra_values)

    def is_valid(self, value: str) -> bool:
        normalized_value = normalize_value(value, self._options)
        return normalized_value in self._normalized_values

    @classmethod
    def get_values_from_csv(cls, path: str, column: str) -> frozenset[str]:
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

        values: list[str] = []

        try:
            parsed_uri: urllib.parse.ParseResult = urllib.parse.urlparse(path)
        except ValueError:
            logging.error(
                f"An error is occured while parsing url using this path: {path}"
            )
            return frozenset({})

        is_valid_scheme: bool = parsed_uri.scheme in ("http", "https", "file")

        if not is_valid_scheme and not os.path.isfile(path):
            raise ValueError(
                f"Invalid path: {path}.The URI must use one of the following schemes: http, https, or file or it must be existing csv file."
            )

        try:
            if is_valid_scheme:
                csvfile = cls.remote_reader.read_file(path)

            else:
                csvfile = cls.local_reader.read_file(path)
        except Exception as e:
            logging.error(f"Error while reading the file at {path}: {e}")
            return frozenset({})

        with csvfile:
            reader: csv.DictReader[str] = csv.DictReader(csvfile)
            try:
                for row in reader:
                    if column in row:
                        values.append(row[column])
                    else:
                        logging.error(f"CSV file is missing the {column} column.")
                        return frozenset({})
            except ValueError:
                logging.error(
                    f"The file associated to this path: {path} is not well csv formatted"
                )
                return frozenset({})
        cls._valid_values = frozenset(values)
        return frozenset(values)

    def get_valid_values_set(self) -> FrozenSet[str]:
        """Returns the canonical set of valid values.

        In the case of versioned data, it will only return the valid values for the version the validator has been initialized with.

        Validation options have no impact on the output - in particular, extra user-defined valid values will not be part of the result.
        """
        return self._valid_values


V = TypeVar("V", bound="Version")


class VersionedSetFormat(SingleSetFormat, Generic[V]):
    """This format defines a closed set of valid values, with different
    versions to choose from.

    Specific implementation details :

    - the type will hint at which version class to use for initializing the format validator.
    - a description of the format can be consulted with `MyClass.metadata.description` or at the top of `help(MyClass)`

    Technical details:

      - In the versioned set format, the `_valid_values` attribute is an instance attribute,
        which takes precedence over the class attribute of the mother class. The
        reason for this is that the exact valid values set is only known on instantiation.
    """

    _versioned_valid_values: VersionedSet = VersionedSet()

    def __init__(self, version: Union[V, str], options: Options = Options()):
        version_id = version if isinstance(version, str) else version.get_id()
        data = self._versioned_valid_values.get_data(version_id)
        if data is None:
            raise ValueError(f"No data available for version: {version_id}")

        self._valid_values = data
        super().__init__(options)


INSEE_SOURCE = "https://www.insee.fr/fr/information/2560452"


@overload
def new(
    class_name: str,
    name: str,
    description: str,
    source: str,
    valid_data: VersionedSet[V],
) -> Type[VersionedSetFormat[V]]: ...


@overload
def new(
    class_name: str, name: str, description: str, source: str, valid_data: FrozenSet
) -> Type[SingleSetFormat]: ...


def new(
    class_name: str,
    name: str,
    description: str,
    source: str,
    valid_data: Union[VersionedSet[V], FrozenSet[str]],
) -> Union[Type[VersionedSetFormat[V]], Type[SingleSetFormat]]:
    """Utility function to create a specialized version of a SetFormat.

    The returned class is a fully featured format that once initialized
    validates data passed as "valid_data" argument.

    If "valid_data" is a VersionedSet, the format will require the
    version to be specified at initialization.
    """
    if isinstance(valid_data, VersionedSet):

        class NewVersionedFormat(VersionedSetFormat):
            _versioned_valid_values = valid_data

        specialized_set_format = NewVersionedFormat

    else:

        class NewFormat(SingleSetFormat):
            _valid_values = valid_data

        specialized_set_format = NewFormat

    specialized_set_format.__name__ = class_name
    specialized_set_format.__qualname__ = class_name
    specialized_set_format.__doc__ = (
        f"{description}\n\n{specialized_set_format.__doc__}"
    )

    specialized_set_format.metadata = Metadata(name, description, source)

    return specialized_set_format
