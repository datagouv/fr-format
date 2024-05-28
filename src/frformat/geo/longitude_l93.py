from frformat import CustomNumericFormat, Metadata
from frformat.geo.latitude_l93 import UnitFormatter

name = "Longitude en Lambert 93"
description = "Vérifie que la longitude en France métropolitaine donnée est une longitude en lambert 93"


class LongitudeL93(CustomNumericFormat):
    metadata = Metadata(name, description)
    formatter = UnitFormatter("m")

    @classmethod
    def is_valid(cls, value: float) -> bool:
        return value >= -357823 and value <= 1313633
