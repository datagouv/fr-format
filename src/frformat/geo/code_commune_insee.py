from typing import Dict, FrozenSet

from frformat import geo_enum_format
from frformat.geo.code_commune_insee_frozenset import (
    CODE_COMMUNE_INSEE_FROZEN_SET_COG_2023,
    CODE_COMMUNE_INSEE_FROZEN_SET_COG_2024,
)
from frformat.geo_enum_format import Millesime

name = "Code commune INSEE"
description = "Vérifie que le code commune correspond bien à un code commune INSEE pour un Code Officiel Géographique donné"

all_cog_versions: Dict[Millesime, FrozenSet[str]] = {
    Millesime.A2023: CODE_COMMUNE_INSEE_FROZEN_SET_COG_2023,
    Millesime.A2024: CODE_COMMUNE_INSEE_FROZEN_SET_COG_2024,
}
CodeCommuneInsee = geo_enum_format.new(
    "CodeCommuneInsee", name, description, all_cog_versions
)
