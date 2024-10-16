from typing import Dict, Set

from frformat import geo_enum_format
from frformat.geo.region_set import REGION_SET_COG_2023, REGION_SET_COG_2024
from frformat.geo_enum_format import Millesime

name = "Nom de région"
description = "Vérifie les régions françaises valides"

all_cog_versions: Dict[Millesime, Set[str]] = {
    Millesime.A2023: REGION_SET_COG_2023,
    Millesime.A2024: REGION_SET_COG_2024,
}
Region = geo_enum_format.new("Region", name, description, all_cog_versions)
