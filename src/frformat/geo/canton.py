from typing import Dict, Set

from frformat import geo_enum_format
from frformat.geo.canton_set import CANTON_SET_COG_2023, CANTON_SET_COG_2024
from frformat.geo_enum_format import Millesime

name = "Nom de canton"
description = (
    "Vérifie que le nom de canton est un canton ou pseudo-canton français valide"
)
all_cog_versions: Dict[Millesime, Set[str]] = {
    Millesime.A2023: CANTON_SET_COG_2023,
    Millesime.A2024: CANTON_SET_COG_2024,
}
Canton = geo_enum_format.new("Canton", name, description, all_cog_versions)
