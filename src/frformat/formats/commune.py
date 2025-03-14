from frformat import set_format
from frformat.formats.commune_frozenset import COMMUNES_COG_2023, COMMUNES_COG_2024
from frformat.set_format import INSEE_SOURCE
from frformat.versioned_set import VersionedSet
from frformat.versions import Millesime

name = "Nom de commune"
description = (
    "Vérifie que le nom correspond à un nom de commune française pour un Code Officiel Géographique donné"
    "(ne vérifie pas l'accentuation, la casse, la ponctuation)"
)
source = INSEE_SOURCE
commune_versioned_data = VersionedSet[Millesime]()
commune_versioned_data.add_version(Millesime.M2023, COMMUNES_COG_2023)
commune_versioned_data.add_version(Millesime.M2024, COMMUNES_COG_2024)

Commune = set_format.new("Commune", name, description, source, commune_versioned_data)
