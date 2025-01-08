from frformat import new_format
from frformat.geo.code_commune_insee_frozenset import (
    CODES_COMMUNES_INSEE_COG_2023,
    CODES_COMMUNES_INSEE_COG_2024,
)
from frformat.new_format import Millesime
from frformat.versioned_set import VersionedSet

name = "Code commune INSEE"
description = "Vérifie que le code commune correspond bien à un code commune INSEE pour un Code Officiel Géographique donné"

code_commune_insee_versioned_data = VersionedSet[Millesime]()
code_commune_insee_versioned_data.add_version(
    Millesime.M2023, CODES_COMMUNES_INSEE_COG_2023
)
code_commune_insee_versioned_data.add_version(
    Millesime.M2024, CODES_COMMUNES_INSEE_COG_2024
)

CodeCommuneInsee = new_format.new(name, description, code_commune_insee_versioned_data)
