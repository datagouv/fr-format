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
        '''Renvoie True si val peut etre une latitude en Lambert 93'''
        return value >= 6037008 and value <= 7230728