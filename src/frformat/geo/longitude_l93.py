from frformat import CustomFloatFormat

name = "Longitude en Lambert 93"
description = "Vérifie que la longitude donnée est une longitude en lambert 93"


class LongitudeL93(CustomFloatFormat):
    @classmethod
    def name(cls) -> str:
        return name

    @classmethod
    def description(cls) -> str:
        return description

    @classmethod
    def is_valid(cls, value: float) -> bool:
        """Renvoie True si value en métre peut etre une longitude en Lambert 93"""
        return value >= -357823 and value <= 1313633
