from frformat.formats.canton_frozenset import CANTON_COG_2023, CANTON_COG_2024
from frformat.set_format import INSEE_SOURCE, new
from frformat.versioned_set import VersionedSet
from frformat.versions import Millesime

name = "Nom de canton"
description = "Canton ou pseudo-canton français pour un Code Officiel Géographique donné"
source = INSEE_SOURCE

canton_versioned_data = VersionedSet[Millesime]()
canton_versioned_data.add_version(Millesime.M2023, CANTON_COG_2023)
canton_versioned_data.add_version(Millesime.M2024, CANTON_COG_2024)

Canton = new("Canton", name, description, source, canton_versioned_data)
