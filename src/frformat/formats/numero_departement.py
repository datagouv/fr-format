from frformat import set_format
from frformat.set_format import INSEE_SOURCE
from frformat.versioned_set import VersionedSet
from frformat.versions import Millesime

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
source = INSEE_SOURCE

numero_departement_versioned_data = VersionedSet[Millesime]()
numero_departement_versioned_data.add_version(
    Millesime.M2023, NUMEROS_DEPARTEMENTS_COG_2023
)
numero_departement_versioned_data.add_version(
    Millesime.M2024, NUMEROS_DEPARTEMENTS_COG_2024
)

NumeroDepartement = set_format.new(
    "NumeroDepartement", name, description, source, numero_departement_versioned_data
)
