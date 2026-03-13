from frformat.set_format import INSEE_SOURCE, new
from frformat.versioned_set import VersionedSet
from frformat.versions import Millesime

CODES_DEPARTEMENTS_COG_2023 = frozenset(
    (
        {str(x).zfill(2) for x in range(1, 20)}
        | {"2A", "2B", "984", "986", "987", "988", "989"}
        | {str(x) for x in range(21, 96)}
        | {str(x) for x in range(971, 979)}
    )
)
CODES_DEPARTEMENTS_COG_2024 = CODES_DEPARTEMENTS_COG_2023

name = "Code du département"
description = "Code de département français, collectivités et territoires d'outre-mer pour un Code Officiel Géographique donné"
source = INSEE_SOURCE

code_departement_versioned_data = VersionedSet[Millesime]()
code_departement_versioned_data.add_version(Millesime.M2023, CODES_DEPARTEMENTS_COG_2023)
code_departement_versioned_data.add_version(Millesime.M2024, CODES_DEPARTEMENTS_COG_2024)

CodeDepartement = new("CodeDepartement", name, description, source, code_departement_versioned_data)
