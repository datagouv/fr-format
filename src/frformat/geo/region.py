from frformat import set_format
from frformat.geo.region_frozenset import REGIONS_COG_2023, REGIONS_COG_2024
from frformat.set_format import Millesime
from frformat.versioned_set import VersionedSet

name = "Nom de région"
description = (
    "Vérifie les régions françaises valides pour un Code Officiel Géographique donné"
)

region_versioned_data = VersionedSet[Millesime]()
region_versioned_data.add_version(Millesime.M2023, REGIONS_COG_2023)
region_versioned_data.add_version(Millesime.M2024, REGIONS_COG_2024)

Region = set_format.new_geo("Region", name, description, region_versioned_data)
