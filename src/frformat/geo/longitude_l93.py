import locale

from frformat import CustomNumericFormat, Metadata
from frformat.common import USPACE
from frformat.geo.latitude_l93 import UnitFormatter

name = "Longitude en Lambert 93"
description = "Vérifie que la longitude en France métropolitaine donnée est une longitude en lambert 93"


class LongitudeL93(CustomNumericFormat):
    metadata = Metadata(name, description)
    formatter = UnitFormatter("m")

    @classmethod
    def is_valid(cls, value: float) -> bool:
        return value >= -357823 and value <= 1313633

    @classmethod
    def _format(cls, value: float) -> str:
        locale.setlocale(locale.LC_ALL, "fr_FR.UTF-8")
        return locale.format_string("%.2f", value, True) + USPACE + "m"
