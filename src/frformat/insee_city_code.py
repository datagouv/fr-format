from frformat.insee_city_code_set import INSEE_CITY_CODE_SET


class InseeCityCode(CustomFormat):
    @classmethod
    def name(cls) -> str:
        return "Code postal"

    @classmethod
    def description(cls) -> str:
        return "Vérifie que le code postal est bien un code postal français"

    @classmethod
    def is_valid(cls, value: str) -> bool:
        return value in POSTAL_CODE_SET
