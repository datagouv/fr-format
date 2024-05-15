import re

from frformat import CustomStrFormat, Metadata
from frformat.common import USPACE

name = "Code RNA"
description = "Vérifie les codes RNA (Répertoire National des Associations) valides"


class CodeRNA(CustomStrFormat):
    metadata = Metadata(name, description)

    @classmethod
    def is_valid(cls, value: str) -> bool:
        return bool(re.match(r"^W\d{9}$", value))

    @classmethod
    def _format(cls, value: str) -> str:
        return f"{value[0:4]}{ USPACE }{value[4:7]}{ USPACE }{value[7:]}"
