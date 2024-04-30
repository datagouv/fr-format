import stdnum.fr.siren

from . import CustomStrFormat


class Siren(CustomStrFormat):
    @classmethod
    def name(cls) -> str:
        return "SIREN"

    @classmethod
    def description(cls) -> str:
        return "Check french SIREN number validity, but does not check if SIREN number exists."

    @classmethod
    def is_valid(cls, value: str) -> bool:
        return stdnum.fr.siren.is_valid(value)

    @classmethod
    def _format(cls, value: str) -> str:
        return f"{value[0:3]} {value[3:6]} {value[6:]}"
