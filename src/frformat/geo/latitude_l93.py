from frformat import CustomFormat

name="Latitude en Lambert 93"
description ="Vérifie que la latitude donnée est une latitude en lambert 93"

class LatitudeL93(CustomFormat):
    
    @classmethod
    def name (cls) -> str:
        return name
    
    @classmethod
    def description (cls) -> str:
        return description

    def float_casting(cls, str2cast: str) -> float :
        return float(str2cast.replace(',', '.'))

    def is_float(cls, val: str) -> bool :
        '''Detects floats, assuming that tables will not have scientific
        notations (3e6) or "+" in the string. "-" is still accepted.'''
        try:
            if any([k in val for k in ['_', '+', 'e', 'E']]):
                return False
            cls.float_casting(cls, val)
            return True
        except ValueError:
            return False 
    
    @classmethod
    def is_valid(cls, val: str) -> bool : 
        '''Renvoie True si val peut etre une latitude en Lambert 93'''
        try:
            return cls.is_float(cls, val) and float(val) >= 6037008 and float(val) <= 7230728
        except ValueError:
            return False
        except OverflowError:
            return False