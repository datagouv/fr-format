from frformat import enum_format
from frformat.geo.code_postal_frozenset import CODE_POSTAL_FROZEN_SET

name = "Code postal"
description = "Vérifie que le code postal est bien un code postal français"

CodePostal = enum_format.new("CodePostal", name, description, CODE_POSTAL_FROZEN_SET)
