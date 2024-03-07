from . import CustomFormat

DEPARTEMENTS_SET = (
    {str(x).zfill(2) for x in range(1, 20)}
    | {"2A", "2B", "984", "986", "987", "988", "989"}
    | {str(x) for x in range(21, 96)}
    | {str(x) for x in range(971, 979)}
)


class NumeroDepartement(CustomFormat):
    @classmethod
    def name(cls) -> str:
        return "Numéro du département"

    @classmethod
    def description(cls) -> str:
        return "Vérifie que le numéro de département correspond bien à un numéro de département français \
            Pour les départements de la Corse, les lettres doivent être en majuscule"

    @classmethod
    def is_valid(cls, value: str) -> bool:
        return value in DEPARTEMENTS_SET
