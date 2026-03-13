from frformat import CustomNumericFormat, Metadata
from frformat.formatter import UnitFormatter

name = "Latitude en Lambert 93"
description = "Latitude en lambert 93 en France métropolitaine"


class LatitudeL93(CustomNumericFormat):
    metadata = Metadata(name, description)
    formatter = UnitFormatter("m")

    def is_valid(self, value: float) -> bool:
        return value >= 6037008 and value <= 7230728
