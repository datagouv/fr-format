from typing import Dict, FrozenSet

from frformat import geo_enum_format
from frformat.geo.departement_frozenset import (
    DEPARTEMENTS_COG_2023,
    DEPARTEMENTS_COG_2024,
)
from frformat.geo_enum_format import Millesime

name = "Nom de département"
description = "Vérifie les départements français, collectivités et territoires d'outre-mer valides pour un Code Officiel Géographique donné"

all_cog_versions: Dict[Millesime, FrozenSet[str]] = {
    Millesime.M2023: DEPARTEMENTS_COG_2023,
    Millesime.M2024: DEPARTEMENTS_COG_2024,
}
Departement = geo_enum_format.new("Departement", name, description, all_cog_versions)
