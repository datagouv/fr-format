from frformat import enum_format
from frformat.geo.code_fantoir_set import CODE_FANTOIR_SET

name = "Code fantoir"
description = "Vérifie les codes fantoirs valides"

CodeFantoir = enum_format.new(name, description, CODE_FANTOIR_SET)
