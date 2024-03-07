from frformat.insee_city_code_set import INSEE_CITY_CODE_SET

from . import CustomFormat


class InseeCityCode(CustomFormat):
    @classmethod
    def name(cls) -> str:
        return "Code commune INSEE"

    @classmethod
    def description(cls) -> str:
        return "Vérifie que le code commune correspond bien à un code commune INSEE"

    @classmethod
    def is_valid(cls, value: str) -> bool:
        return value in INSEE_CITY_CODE_SET
