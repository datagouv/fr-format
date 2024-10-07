from typing import Dict, Set

from frformat import enum_format

CODE_REGION_SET_COG_2023 = {
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
CODE_REGION_SET_COG_2024 = CODE_REGION_SET_COG_2023

name = "Code région"
description = (
    "Vérifie qu'il s'agit d'un code région selon le code officiel géographique donné"
)
all_cog_version: Dict[str, Set[str]] = {
    "COG_2024": CODE_REGION_SET_COG_2024,
    "COG_2023": CODE_REGION_SET_COG_2023,
}
CodeRegion = enum_format.new("CodeRegion", name, description, all_cog_version)
