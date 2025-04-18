from frformat import set_format
from frformat.formats.departement_frozenset import (
    DEPARTEMENTS_COG_2023,
    DEPARTEMENTS_COG_2024,
)
from frformat.set_format import INSEE_SOURCE
from frformat.versioned_set import VersionedSet
from frformat.versions import Millesime

name = "Nom de département"
description = "Vérifie les départements français, collectivités et territoires d'outre-mer valides pour un Code Officiel Géographique donné"
source = INSEE_SOURCE
departement_versioned_data = VersionedSet[Millesime]()
departement_versioned_data.add_version(Millesime.M2023, DEPARTEMENTS_COG_2023)
departement_versioned_data.add_version(Millesime.M2024, DEPARTEMENTS_COG_2024)

Departement = set_format.new(
    "Departement", name, description, source, departement_versioned_data
)
