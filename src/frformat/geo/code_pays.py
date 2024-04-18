from frformat import enum_format
from frformat.geo.code_pays_set import CODE_PAYS_ISO2_SET, CODE_PAYS_ISO3_SET

name = "Codes ISO2 Pays"
description = "Code ISO 2 de pays selon COG2024"

CodePaysISO2 = enum_format.new(name, description, CODE_PAYS_ISO2_SET)

name = "Codes ISO3 Pays"
description = "Code ISO 3 de pays selon COG2024"

CodePaysISO3 = enum_format.new(name, description, CODE_PAYS_ISO3_SET)
