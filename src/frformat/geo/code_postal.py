from frformat import new_format
from frformat.geo.code_postal_frozenset import CODES_POSTAUX

name = "Code postal"
description = "Vérifie que le code postal est bien un code postal français"

CodePostal = new_format.new(name, description, CODES_POSTAUX)
