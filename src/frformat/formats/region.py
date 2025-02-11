from frformat import set_format
from frformat.formats.region_frozenset import (
    REGIONS_COG_2015,
    REGIONS_COG_2016,
    REGIONS_SINCE_2017,
)
from frformat.set_format import INSEE_SOURCE, Millesime
from frformat.versioned_set import VersionedSet

name = "Nom de région"
description = (
    "Vérifie les régions françaises valides pour un Code Officiel Géographique donné"
)
source = INSEE_SOURCE
versions = [
    Millesime.M2017,
    Millesime.M2018,
    Millesime.M2019,
    Millesime.M2020,
    Millesime.M2021,
    Millesime.M2022,
    Millesime.M2023,
    Millesime.M2024,
]

region_versioned_data = VersionedSet[Millesime]()
region_versioned_data.add_version(Millesime.M2015, REGIONS_COG_2015)
region_versioned_data.add_version(Millesime.M2016, REGIONS_COG_2016)

for v in versions:
    region_versioned_data.add_version(v, REGIONS_SINCE_2017)

Region = set_format.new("Region", name, description, source, region_versioned_data)
