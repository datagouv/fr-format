from frformat import geo_format
from frformat.geo.canton_frozenset import CANTON_COG_2023, CANTON_COG_2024
from frformat.geo_format import Millesime
from frformat.versioned_set import VersionedSet

name = "Nom de canton"
description = "Vérifie que le nom de canton est un canton ou pseudo-canton français valide pour un Code Officiel Géographique donné"

canton_versioned_data = VersionedSet[Millesime]()
canton_versioned_data.add_version(Millesime.M2023, CANTON_COG_2023)
canton_versioned_data.add_version(Millesime.M2024, CANTON_COG_2024)

Canton = geo_format.new("Canton", name, description, canton_versioned_data)
