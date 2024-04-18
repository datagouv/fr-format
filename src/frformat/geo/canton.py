from frformat import enum_format
from frformat.geo.canton_set import CANTON_SET

name = "Nom de canton"
description = (
    "Vérifie que le nom de canton est un canton ou pseudo-canton français valide"
)

Canton = enum_format.new(name, description, CANTON_SET)
