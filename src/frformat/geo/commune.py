from typing import Dict, Set

from frformat import geo_enum_format
from frformat.geo.commune_set import COMMUNE_SET_COG_2023, COMMUNE_SET_COG_2024
from frformat.geo_enum_format import Millesime

name = "Nom de commune"
description = (
    "Vérifie que le nom correspond à un nom de commune française pour un Code Officiel Géographique donné"
    "(ne vérifie pas l'accentuation, la casse, la ponctuation)"
)

all_cog_versions: Dict[Millesime, Set[str]] = {
    Millesime.A2023: COMMUNE_SET_COG_2023,
    Millesime.A2024: COMMUNE_SET_COG_2024,
}
Commune = geo_enum_format.new("Commune", name, description, all_cog_versions)
