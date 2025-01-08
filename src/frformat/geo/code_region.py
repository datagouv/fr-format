from frformat import geo_format
from frformat.versioned_set import VersionedSet

from ..geo_format import Millesime

CODES_REGIONS_COG_2023 = frozenset(
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
CODES_REGIONS_COG_2024 = CODES_REGIONS_COG_2023

name = "Code région"
description = "Vérifie qu'il s'agit d'un code région selon le Code Officiel Géographique (cog) donné"

code_region_versioned_data = VersionedSet[Millesime]()
code_region_versioned_data.add_version(Millesime.M2023, CODES_REGIONS_COG_2023)
code_region_versioned_data.add_version(Millesime.M2024, CODES_REGIONS_COG_2024)

CodeRegion = geo_format.new("CodeRegion", name, description, code_region_versioned_data)
