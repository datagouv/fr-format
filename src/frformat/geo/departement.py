from frformat import geo_enum_format
from frformat.geo.departement_frozenset import (
    DEPARTEMENTS_COG_2023,
    DEPARTEMENTS_COG_2024,
)
from frformat.geo_enum_format import Millesime
from frformat.versioned_set import VersionedSet

name = "Nom de département"
description = "Vérifie les départements français, collectivités et territoires d'outre-mer valides pour un Code Officiel Géographique donné"

departement_versioned_data = VersionedSet()
departement_versioned_data.add_version(Millesime.M2023, DEPARTEMENTS_COG_2023)
departement_versioned_data.add_version(Millesime.M2024, DEPARTEMENTS_COG_2024)

Departement = geo_enum_format.new(
    "Departement", name, description, departement_versioned_data
)
