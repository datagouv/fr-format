import stdnum.fr.siret

from . import CustomStrFormat, Metadata

name = "SIRET"
description = (
    "Check french SIRET number validity, but does not check if SIRET number exists."
)


class Siret(CustomStrFormat):
    metadata = Metadata(name, description)

    @classmethod
    def is_valid(cls, value: str) -> bool:
        return stdnum.fr.siret.is_valid(value)

    @classmethod
    def _format(cls, value: str) -> str:
        return f"{value[0:9]} {value[9:]}"
