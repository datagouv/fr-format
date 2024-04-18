from frformat import enum_format
from frformat.geo.pays_set import PAYS_SET

name = "Pays et territoires étrangers"
description = "Nom de pays et territoires étrangers selon COG2024"

Pays = enum_format.new(name, description, PAYS_SET)
