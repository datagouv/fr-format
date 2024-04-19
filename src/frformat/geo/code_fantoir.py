import re

from frformat import CustomFormat
from frformat.geo.code_fantoir_set import PARTIAL_CODE_FANTOIR_SET

name = "Code fantoir"
description = "Vérifie les codes fantoirs valides"


class CodeFantoir(CustomFormat):
    @classmethod
    def name(cls) -> str:
        return "SIREN"

    @classmethod
    def description(cls) -> str:
        return "Check french SIREN number validity, but does not check if SIREN number exists."

    @classmethod
    def is_valid(cls, value: str) -> bool:
        if not bool(re.match(r"^[0-9A-Z]{2}[0-9]{2}[ABCDEFGHJKLMNPRSTUVWXYZ]$", value)):
            return False

        return value[:4] in PARTIAL_CODE_FANTOIR_SET

    @classmethod
    def _format(cls, value: str) -> str:
        return f"{value[0:3]} {value[3:6]} {value[6:]}"
