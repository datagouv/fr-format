import re

from frformat import CustomStrFormat, Formatter, Metadata
from frformat.common import USPACE

name = "Code RNA"
description = "Vérifie les codes RNA (Répertoire National des Associations) valides"


class RNAFormatter(Formatter):
    def format(self, value: str) -> str:
        return f"{value[0:4]}{ USPACE }{value[4:7]}{ USPACE }{value[7:]}"


class CodeRNA(CustomStrFormat):
    metadata = Metadata(name, description)
    formatter = RNAFormatter()

    @classmethod
    def is_valid(cls, value: str) -> bool:
        return bool(re.match(r"^W\d{9}$", value))
