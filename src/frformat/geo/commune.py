from frformat import enum_format
from frformat.geo.commune_set import COMMUNE_SET

name = "Nom de commune"
description = (
    "Vérifie que le nom correspond à un nom de commune française "
    "(ne vérifie pas l'accentuation, la casse, la ponctuation)"
)

Commune = enum_format.new("Commune", name, description, COMMUNE_SET)
