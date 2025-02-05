from frformat import set_format
from frformat.formats.canton_frozenset import CANTON_COG_2023, CANTON_COG_2024
from frformat.set_format import INSEE_SOURCE, Millesime
from frformat.versioned_set import VersionedSet

name = "Nom de canton"
description = "Vérifie que le nom de canton est un canton ou pseudo-canton français valide pour un Code Officiel Géographique donné"
source = INSEE_SOURCE

canton_versioned_data = VersionedSet[Millesime]()
canton_versioned_data.add_version(Millesime.M2023, CANTON_COG_2023)
canton_versioned_data.add_version(Millesime.M2024, CANTON_COG_2024)

Canton = set_format.new("Canton", name, description, source, canton_versioned_data)
