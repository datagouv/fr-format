from frformat import set_format
from frformat.set_format import INSEE_SOURCE, Millesime
from frformat.versioned_set import VersionedSet

CODES_REGION_REPETES = frozenset(
    {
        "01",
        "02",
        "03",
        "04",
        "06",
        "11",
        "24",
        "52",
        "53",
        "93",
        "94",
    }
)
CODES_REGIONS_COG_2015 = CODES_REGION_REPETES.union(frozenset(
            {
                "21",
                "22",
                "23",
                "25",
                "26",
                "31",
                "41",
                "42",
                "43",
                "54",
                "72",
                "73",
                "74",
                "83",
                "91",
            }
        ))
CODES_REGIONS_COG_2016 = CODES_REGION_REPETES.union( frozenset(
            {
                "27",
                "28",
                "32",
                "44",
                "75",
                "76",
                "84",
            }
        ))
CODES_REGIONS_COG_2023 = CODES_REGIONS_COG_2016
CODES_REGIONS_COG_2024 = CODES_REGIONS_COG_2016

name = "Code région"
description = "Vérifie qu'il s'agit d'un code région selon le Code Officiel Géographique (cog) donné, sachant qu'à partir du Millesime 2016 la liste des régions française change suite à plusieurs fusions"
source = INSEE_SOURCE

code_region_versioned_data = VersionedSet[Millesime]()
code_region_versioned_data.add_version(Millesime.M2015, CODES_REGIONS_COG_2015)
code_region_versioned_data.add_version(Millesime.M2016, CODES_REGIONS_COG_2016)
code_region_versioned_data.add_version(Millesime.M2023, CODES_REGIONS_COG_2023)
code_region_versioned_data.add_version(Millesime.M2024, CODES_REGIONS_COG_2024)

CodeRegion = set_format.new(
    "CodeRegion", name, description, source, code_region_versioned_data
)
