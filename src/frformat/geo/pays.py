from typing import Dict, Set

from frformat import geo_enum_format
from frformat.geo.pays_set import PAYS_SET_COG_2024
from frformat.geo_enum_format import Millesime

name = "Pays et territoires étrangers"
description = "Nom de pays et territoires étrangers selon COG2024 et COG2023"

all_cog_versions: Dict[Millesime, Set[str]] = {
    Millesime.A2024: PAYS_SET_COG_2024,
}

Pays = geo_enum_format.new("Pays", name, description, all_cog_versions)
