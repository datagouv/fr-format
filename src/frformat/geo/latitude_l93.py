import locale

from frformat import CustomFloatFormat

name = "Latitude en Lambert 93"
description = "Vérifie que la latitude en France métropolitaine donnée est une latitude en lambert 93"


class LatitudeL93(CustomFloatFormat):
    @classmethod
    def name(cls) -> str:
        return name

    @classmethod
    def description(cls) -> str:
        return description

    @classmethod
    def is_valid(cls, value: float) -> bool:
        return value >= 6037008 and value <= 7230728

    @classmethod
    def _format(cls, value: float) -> str:
        locale.setlocale(locale.LC_ALL, "fr_FR.UTF-8")
        return locale.format_string("%.2f", value)
