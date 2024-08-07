from frformat import enum_format
from frformat.geo.region_set import REGION_SET

name = "Nom de région"
description = (
    "Vérifie les régions françaises valides (code officiel géographique 2020) "
)

Region = enum_format.new("Region", name, description, REGION_SET)
