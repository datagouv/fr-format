from frformat import CustomNumericFormat, Metadata
from frformat.formats.latitude_l93 import UnitFormatter

name = "Longitude en Lambert 93"
description = "Longitude en lambert 93 en France métropolitaine"


class LongitudeL93(CustomNumericFormat):
    metadata = Metadata(name, description)
    formatter = UnitFormatter("m")

    def is_valid(self, value: float) -> bool:
        return value >= -357823 and value <= 1313633
