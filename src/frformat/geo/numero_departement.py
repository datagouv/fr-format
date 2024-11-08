from typing import Dict, FrozenSet

from frformat import geo_enum_format
from frformat.geo_enum_format import Millesime

NUMEROS_DEPARTEMENTS_COG_2023 = frozenset(
    (
        {str(x).zfill(2) for x in range(1, 20)}
        | {"2A", "2B", "984", "986", "987", "988", "989"}
        | {str(x) for x in range(21, 96)}
        | {str(x) for x in range(971, 979)}
    )
)
NUMEROS_DEPARTEMENTS_COG_2024 = NUMEROS_DEPARTEMENTS_COG_2023

name = "Numéro du département"
description = "Vérifie que le numéro de département correspond bien à un numéro de département français, collectivités et territoires d'outre-mer pour un Code Officiel Géographique donné"

all_cog_versions: Dict[Millesime, FrozenSet[str]] = {
    Millesime.M2023: NUMEROS_DEPARTEMENTS_COG_2023,
    Millesime.M2024: NUMEROS_DEPARTEMENTS_COG_2024,
}
NumeroDepartement = geo_enum_format.new(
    "NumeroDepartement", name, description, all_cog_versions
)
