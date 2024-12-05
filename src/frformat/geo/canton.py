from typing import Dict, FrozenSet

from frformat import geo_enum_format
from frformat.geo.canton_frozenset import CANTON_COG_2023, CANTON_COG_2024
from frformat.geo_enum_format import Millesime

name = "Nom de canton"
description = "Vérifie que le nom de canton est un canton ou pseudo-canton français valide pour un Code Officiel Géographique donné"
all_cog_versions: Dict[Millesime, FrozenSet[str]] = {
    Millesime.M2023: CANTON_COG_2023,
    Millesime.M2024: CANTON_COG_2024,
}
Canton = geo_enum_format.new("Canton", name, description, all_cog_versions)
