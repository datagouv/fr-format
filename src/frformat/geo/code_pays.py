from frformat import new_format
from frformat.geo.code_pays_frozenset import (
    CODES_PAYS_ISO2_COG_2023,
    CODES_PAYS_ISO2_COG_2024,
    CODES_PAYS_ISO3_COG_2023,
    CODES_PAYS_ISO3_COG_2024,
)
from frformat.new_format import Millesime
from frformat.versioned_set import VersionedSet

name = "Codes ISO2 Pays"
description = "Code ISO 2 de pays pour un Code Officiel Géographique donné"

code_pays_IS02_versioned_data = VersionedSet[Millesime]()
code_pays_IS02_versioned_data.add_version(Millesime.M2023, CODES_PAYS_ISO2_COG_2023)
code_pays_IS02_versioned_data.add_version(Millesime.M2024, CODES_PAYS_ISO2_COG_2024)

CodePaysISO2 = new_format.new(name, description, code_pays_IS02_versioned_data)


name = "Codes ISO3 Pays"
description = "Code ISO 3 de pays pour un Code Officiel Géographique donné"

code_pays_IS03_versioned_data = VersionedSet[Millesime]()
code_pays_IS03_versioned_data.add_version(Millesime.M2023, CODES_PAYS_ISO3_COG_2023)
code_pays_IS03_versioned_data.add_version(Millesime.M2024, CODES_PAYS_ISO3_COG_2024)

CodePaysISO3 = new_format.new(name, description, code_pays_IS03_versioned_data)
