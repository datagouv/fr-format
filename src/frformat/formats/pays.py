from frformat import set_format
from frformat.formats.pays_frozenset import PAYS_COG_2024
from frformat.set_format import INSEE_SOURCE, Millesime
from frformat.versioned_set import VersionedSet

name = "Pays et territoires étrangers"
description = (
    "Nom de pays et territoires étrangers pour un Code Officiel Géographique donné"
)
source = INSEE_SOURCE

pays_versioned_data = VersionedSet[Millesime]()
pays_versioned_data.add_version(Millesime.M2024, PAYS_COG_2024)

Pays = set_format.new("Pays", name, description, source, pays_versioned_data)
