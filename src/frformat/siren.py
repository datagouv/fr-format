import stdnum.fr.siren

from frformat.formatter import Formatter

from . import CustomStrFormat, Metadata

name = "SIREN"
description = (
    "Check french SIREN number validity, but does not check if SIREN number exists."
)


class SirenFormatter(Formatter):
    def format(self, value: str) -> str:
        return f"{value[0:3]} {value[3:6]} {value[6:]}"


class Siren(CustomStrFormat):
    metadata = Metadata(name, description)
    formatter = SirenFormatter()

    @classmethod
    def is_valid(cls, value: str) -> bool:
        return stdnum.fr.siren.is_valid(value)
