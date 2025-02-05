from frformat import set_format
from frformat.set_format import INSEE_SOURCE, Millesime
from frformat.versioned_set import VersionedSet

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
source = INSEE_SOURCE

code_region_versioned_data = VersionedSet[Millesime]()
code_region_versioned_data.add_version(Millesime.M2023, CODES_REGIONS_COG_2023)
code_region_versioned_data.add_version(Millesime.M2024, CODES_REGIONS_COG_2024)

CodeRegion = set_format.new(
    "CodeRegion", name, description, source, code_region_versioned_data
)
