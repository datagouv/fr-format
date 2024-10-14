from typing import Dict, Set

from frformat import geo_enum_format
from frformat.geo.commune_set import COMMUNE_SET_COG_2023, COMMUNE_SET_COG_2024
from frformat.geo_enum_format import Millesime

name = "Nom de commune"
description = (
    "Vérifie que le nom correspond à un nom de commune française ( depuis le Code Officiel Géographique 2023) "
    "(ne vérifie pas l'accentuation, la casse, la ponctuation)"
)

all_cog_version: Dict[Millesime, Set[str]] = {
    Millesime.Y2023: COMMUNE_SET_COG_2023,
    Millesime.Y2024: COMMUNE_SET_COG_2024,
}
Commune = geo_enum_format.new("Commune", name, description, all_cog_version)
