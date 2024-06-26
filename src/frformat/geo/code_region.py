from frformat import enum_format

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

name = "Code région"
description = (
    "Vérifie qu'il s'agit d'un code région selon le code officiel géographique 2024"
)

CodeRegion = enum_format.new("CodeRegion", name, description, CODE_REGION_SET)
