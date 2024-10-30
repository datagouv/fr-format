from typing import Dict, Set

from frformat import geo_enum_format
from frformat.geo.departement_set import (
    DEPARTEMENT_SET_COG_2023,
    DEPARTEMENT_SET_COG_2024,
)
from frformat.geo_enum_format import Millesime

name = "Nom de département"
description = (
    "Vérifie les départements français valides pour un Code Officiel Géographique donné"
)

all_cog_versions: Dict[Millesime, Set[str]] = {
    Millesime.A2023: DEPARTEMENT_SET_COG_2023,
    Millesime.A2024: DEPARTEMENT_SET_COG_2024,
}
Departement = geo_enum_format.new("Departement", name, description, all_cog_versions)
