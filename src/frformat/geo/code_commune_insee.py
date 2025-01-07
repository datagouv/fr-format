from typing import Dict, FrozenSet

from frformat import geo_enum_format
from frformat.geo.code_commune_insee_frozenset import (
    INTERSECTION_CODE_COMMUNE_INSEE,
    SPECIFIC_VALUES_CODE_COMMUNES_INSEE_COG_2023,
    SPECIFIC_VALUES_CODE_COMMUNES_INSEE_COG_2024,
)
from frformat.geo_enum_format import Millesime

name = "Code commune INSEE"
description = "Vérifie que le code commune correspond bien à un code commune INSEE pour un Code Officiel Géographique donné"

all_cog_versions: Dict[Millesime, FrozenSet[str]] = {
    Millesime.M2023: SPECIFIC_VALUES_CODE_COMMUNES_INSEE_COG_2023,
    Millesime.M2024: SPECIFIC_VALUES_CODE_COMMUNES_INSEE_COG_2024,
    Millesime.INTERSECTION: INTERSECTION_CODE_COMMUNE_INSEE,
}
CodeCommuneInsee = geo_enum_format.new(
    "CodeCommuneInsee", name, description, all_cog_versions
)
