from frformat.formats.code_commune_insee_frozenset import (
    CODES_COMMUNES_INSEE_COG_2023,
    CODES_COMMUNES_INSEE_COG_2024,
)
from frformat.set_format import INSEE_SOURCE, new
from frformat.versioned_set import VersionedSet
from frformat.versions import Millesime

name = "Code commune INSEE"
description = "Code commune INSEE pour un Code Officiel Géographique donné"
source = INSEE_SOURCE

code_commune_insee_versioned_data = VersionedSet[Millesime]()
code_commune_insee_versioned_data.add_version(Millesime.M2023, CODES_COMMUNES_INSEE_COG_2023)
code_commune_insee_versioned_data.add_version(Millesime.M2024, CODES_COMMUNES_INSEE_COG_2024)

CodeCommuneInsee = new(
    "CodeCommuneInsee", name, description, source, code_commune_insee_versioned_data
)
