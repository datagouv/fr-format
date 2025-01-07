from frformat import geo_format
from frformat.geo.departement_frozenset import (
    DEPARTEMENTS_COG_2023,
    DEPARTEMENTS_COG_2024,
)
from frformat.geo_format import Millesime
from frformat.versioned_set import VersionedSet

name = "Nom de département"
description = "Vérifie les départements français, collectivités et territoires d'outre-mer valides pour un Code Officiel Géographique donné"

departement_versioned_data = VersionedSet[Millesime]()
departement_versioned_data.add_version(Millesime.M2023, DEPARTEMENTS_COG_2023)
departement_versioned_data.add_version(Millesime.M2024, DEPARTEMENTS_COG_2024)

Departement = geo_format.new(
    "Departement", name, description, departement_versioned_data
)
