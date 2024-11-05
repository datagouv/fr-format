from typing import Dict, FrozenSet

from frformat import geo_enum_format
from frformat.geo.commune_frozenset import COMMUNES_COG_2023, COMMUNES_COG_2024
from frformat.geo_enum_format import Millesime

name = "Nom de commune"
description = (
    "Vérifie que le nom correspond à un nom de commune française pour un Code Officiel Géographique donné"
    "(ne vérifie pas l'accentuation, la casse, la ponctuation)"
)

all_cog_versions: Dict[Millesime, FrozenSet[str]] = {
    Millesime.A2023: COMMUNES_COG_2023,
    Millesime.A2024: COMMUNES_COG_2024,
}
Commune = geo_enum_format.new("Commune", name, description, all_cog_versions)
