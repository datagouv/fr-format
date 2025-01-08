from frformat import new_format
from frformat.geo.pays_frozenset import PAYS_COG_2024
from frformat.new_format import Millesime
from frformat.versioned_set import VersionedSet

name = "Pays et territoires étrangers"
description = (
    "Nom de pays et territoires étrangers pour un Code Officiel Géographique donné"
)

pays_versioned_data = VersionedSet[Millesime]()
pays_versioned_data.add_version(Millesime.M2024, PAYS_COG_2024)

Pays = new_format.new(name, description, pays_versioned_data)
