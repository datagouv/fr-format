from frformat import CustomFloatFormat

name="Latitude en Lambert 93"
description ="Vérifie que la latitude donnée est une latitude en lambert 93"

class LatitudeL93(CustomFloatFormat):
    
    @classmethod
    def name (cls) -> str:
        return name
    
    @classmethod
    def description (cls) -> str:
        return description

    @classmethod
    def is_valid(cls, value: float) -> bool : 
        '''Renvoie True si val en degrés peut etre une latitude en Lambert 93'''
        return value >= 41 and value <= 51.4