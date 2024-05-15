import re

from frformat import CustomStrFormat, Metadata
from frformat.formatter import Formatter
from frformat.geo.code_fantoir_set import PARTIAL_CODE_FANTOIR_SET

name = "Code fantoir"
description = "Vérifie les codes fantoirs valides"


class CodeFantoirFormatter(Formatter):
    def format(self, value: str) -> str:
        return f"{value[0:3]} {value[3:6]} {value[6:]}"


class CodeFantoir(CustomStrFormat):
    metadata = Metadata(name, description)
    formatter = CodeFantoirFormatter()

    @classmethod
    def is_valid(cls, value: str) -> bool:
        if not bool(re.match(r"^[0-9A-Z]{2}[0-9]{2}[ABCDEFGHJKLMNPRSTUVWXYZ]$", value)):
            return False

        return value[:4] in PARTIAL_CODE_FANTOIR_SET
