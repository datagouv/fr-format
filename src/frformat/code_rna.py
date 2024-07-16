import re

from frformat import CustomStrFormat, Formatter, Metadata
from frformat.common import NNBSP

name = "Code RNA"
description = "Vérifie les codes RNA (Répertoire National des Associations) valides"


class RNAFormatter(Formatter):
    def format(self, value: str) -> str:
        return f"{value[0:4]}{ NNBSP }{value[4:7]}{ NNBSP }{value[7:]}"


class CodeRNA(CustomStrFormat):
    metadata = Metadata(name, description)
    formatter = RNAFormatter()

    def is_valid(self, value: str) -> bool:
        return bool(re.match(r"^W\d{9}$", value))
