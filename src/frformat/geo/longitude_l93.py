import locale

from frformat import CustomFloatFormat

name = "Longitude en Lambert 93"
description = "Vérifie que la longitude en France métropolitaine donnée est une longitude en lambert 93"


class LongitudeL93(CustomFloatFormat):
    @classmethod
    def name(cls) -> str:
        return name

    @classmethod
    def description(cls) -> str:
        return description

    @classmethod
    def is_valid(cls, value: float) -> bool:
        return value >= -357823 and value <= 1313633

    @classmethod
    def _format(cls, value: float) -> str:
        locale.setlocale(locale.LC_ALL, "fr_FR.UTF-8")
        return locale.format_string("%.2f", value, True) + "\u00A0m"
