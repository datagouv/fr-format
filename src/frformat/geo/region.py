from frformat import enum_format
from frformat.geo.region_set import REGION_SET

name = "Nom de région"
description = (
    "Vérifie les régions françaises valides (code officiel géographique 2020) "
    "(ne vérifie pas l'accentuation, la casse, la ponctuation)"
)
enum = REGION_SET

Region = enum_format.new(name, description, enum)
