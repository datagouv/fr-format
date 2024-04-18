from frformat import enum_format
from frformat.geo.code_commune_insee_set import CODE_COMMUNE_INSEE_SET

name = "Code commune INSEE"
description = "Vérifie que le code commune correspond bien à un code commune INSEE"

CodeCommuneInsee = enum_format.new(name, description, CODE_COMMUNE_INSEE_SET)
