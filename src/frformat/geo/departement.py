from frformat import enum_format
from frformat.geo.departement_set import DEPARTEMENT_SET

name = "Nom de département"
description = (
    "Vérifie les départements français valides (code officiel géographique 2020)"
)

Departement = enum_format.new("Departement", name, description, DEPARTEMENT_SET)
