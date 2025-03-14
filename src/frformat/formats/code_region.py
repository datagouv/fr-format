from frformat import set_format
from frformat.set_format import INSEE_SOURCE
from frformat.versioned_set import VersionedSet
from frformat.versions import Millesime

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
CODES_REGIONS_COG_2015 = CODES_REGION_REPETES.union(
    frozenset(
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
    )
)
CODES_REGIONS_SINCE_2016 = CODES_REGION_REPETES.union(
    frozenset(
        {
            "27",
            "28",
            "32",
            "44",
            "75",
            "76",
            "84",
        }
    )
)

name = "Code région"
description = "Vérifie qu'il s'agit d'un code région selon le Code Officiel Géographique (cog) donné. À partir du Millesime 2016 la liste des régions françaises change suite à plusieurs fusions"
source = INSEE_SOURCE
versions = [
    Millesime.M2016,
    Millesime.M2017,
    Millesime.M2018,
    Millesime.M2019,
    Millesime.M2020,
    Millesime.M2021,
    Millesime.M2022,
    Millesime.M2023,
    Millesime.M2024,
]

code_region_versioned_data = VersionedSet[Millesime]()
code_region_versioned_data.add_version(Millesime.M2015, CODES_REGIONS_COG_2015)

for v in versions:
    code_region_versioned_data.add_version(v, CODES_REGIONS_SINCE_2016)

CodeRegion = set_format.new(
    "CodeRegion", name, description, source, code_region_versioned_data
)
