from typing import Dict, FrozenSet

from frformat import geo_enum_format
from frformat.geo.pays_frozenset import PAYS_COG_2024
from frformat.geo_enum_format import Millesime

name = "Pays et territoires étrangers"
description = (
    "Nom de pays et territoires étrangers pour un Code Officiel Géographique donné"
)

all_cog_versions: Dict[Millesime, FrozenSet[str]] = {
    Millesime.M2024: PAYS_COG_2024,
}

Pays = geo_enum_format.new("Pays", name, description, all_cog_versions)
