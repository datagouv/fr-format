from frformat import CustomFormat


class CodeRegion(CustomFormat):
    @classmethod
    def name(cls) -> str:
        return "Code région"

    @classmethod
    def description(cls) -> str:
        return (
            "Vérifie qu'il s'agit d'un code région selon le code officiel "
            "géographique 2020"
        )

    @classmethod
    def is_valid(cls, value: str) -> bool:
        return value in CODE_REGION_SET


CODE_REGION_SET = {
    "01",
    "02",
    "03",
    "04",
    "06",
    "11",
    "24",
    "27",
    "28",
    "32",
    "44",
    "52",
    "53",
    "75",
    "76",
    "84",
    "93",
    "94",
}
