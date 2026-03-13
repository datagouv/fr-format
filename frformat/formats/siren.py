import stdnum.fr.siren

from frformat.common import NNBSP
from frformat.formatter import Formatter

from .. import CustomStrFormat, Metadata

name = "SIREN"
description = "Numéro SIREN (vérifie la validité intrinsèque, mais pas l'attribution du SIREN)"


class SirenFormatter(Formatter):
    def format(self, value: str) -> str:
        return f"{value[0:3]}{NNBSP}{value[3:6]}{NNBSP}{value[6:]}"


class Siren(CustomStrFormat):
    metadata = Metadata(name, description)
    formatter = SirenFormatter()

    def is_valid(self, value: str) -> bool:
        return stdnum.fr.siren.is_valid(value)
