from frformat import CustomFloatFormat, Metadata
from frformat.formatter import UnitFormatter

name = "Latitude en Lambert 93"
description = "Vérifie que la latitude en France métropolitaine donnée est une latitude en lambert 93"


class LatitudeL93(CustomFloatFormat):
    metadata = Metadata(name, description)
    formatter = UnitFormatter("m")

    @classmethod
    def is_valid(cls, value: float) -> bool:
        return value >= 6037008 and value <= 7230728
