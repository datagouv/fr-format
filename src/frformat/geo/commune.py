from frformat import geo_format
from frformat.geo.commune_frozenset import COMMUNES_COG_2023, COMMUNES_COG_2024
from frformat.geo_format import Millesime
from frformat.versioned_set import VersionedSet

name = "Nom de commune"
description = (
    "Vérifie que le nom correspond à un nom de commune française pour un Code Officiel Géographique donné"
    "(ne vérifie pas l'accentuation, la casse, la ponctuation)"
)

commune_versioned_data = VersionedSet[Millesime]()
commune_versioned_data.add_version(Millesime.M2023, COMMUNES_COG_2023)
commune_versioned_data.add_version(Millesime.M2024, COMMUNES_COG_2024)

Commune = geo_format.new("Commune", name, description, commune_versioned_data)
