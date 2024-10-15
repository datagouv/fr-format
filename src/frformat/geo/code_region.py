from typing import Dict, Set

from frformat import geo_enum_format

from ..geo_enum_format import Millesime

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
description = "Vérifie qu'il s'agit d'un code région selon le code officiel géographique (cog) donné"
all_cog_versions: Dict[Millesime, Set[str]] = {
    Millesime.A2023: CODE_REGION_SET_COG_2023,
    Millesime.A2024: CODE_REGION_SET_COG_2024,
}
CodeRegion = geo_enum_format.new("CodeRegion", name, description, all_cog_versions)
