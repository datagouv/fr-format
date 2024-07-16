import stdnum.fr.siret

from frformat.common import NNBSP
from frformat.formatter import Formatter

from . import CustomStrFormat, Metadata

name = "SIRET"
description = (
    "Check french SIRET number validity, but does not check if SIRET number exists."
)


class SiretFormatter(Formatter):
    def format(self, value: str) -> str:
        return f"{value[0:9]}{ NNBSP }{value[9:]}"


class Siret(CustomStrFormat):
    metadata = Metadata(name, description)
    formatter = SiretFormatter()

    def is_valid(self, value: str) -> bool:
        return stdnum.fr.siret.is_valid(value)
