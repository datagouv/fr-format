from frformat import set_format
from frformat.formats.code_postal_frozenset import CODES_POSTAUX

name = "Code postal"
description = "Vérifie que le code postal est bien un code postal français"
source = ""

CodePostal = set_format.new("CodePostal", name, description, source, CODES_POSTAUX)
