from typing import Dict, FrozenSet

from frformat import geo_enum_format

from ..geo_enum_format import Millesime

CODE_REGION_FROZEN_SET_COG_2023 = frozenset(
    {
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
)
CODE_REGION_FROZEN_SET_COG_2024 = CODE_REGION_FROZEN_SET_COG_2023

name = "Code région"
description = "Vérifie qu'il s'agit d'un code région selon le Code Officiel Géographique (cog) donné"
all_cog_versions: Dict[Millesime, FrozenSet[str]] = {
    Millesime.A2023: CODE_REGION_FROZEN_SET_COG_2023,
    Millesime.A2024: CODE_REGION_FROZEN_SET_COG_2024,
}
CodeRegion = geo_enum_format.new("CodeRegion", name, description, all_cog_versions)
