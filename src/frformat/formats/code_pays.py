from frformat import set_format
from frformat.formats.code_pays_frozenset import (
    CODES_PAYS_ISO2_COG_2023,
    CODES_PAYS_ISO2_COG_2024,
    CODES_PAYS_ISO3_COG_2023,
    CODES_PAYS_ISO3_COG_2024,
)
from frformat.set_format import INSEE_SOURCE
from frformat.versioned_set import VersionedSet
from frformat.versions import Millesime

name = "Codes ISO2 Pays"
description = "Code ISO 2 de pays pour un Code Officiel Géographique donné"
source = INSEE_SOURCE

code_pays_IS02_versioned_data = VersionedSet[Millesime]()
code_pays_IS02_versioned_data.add_version(Millesime.M2023, CODES_PAYS_ISO2_COG_2023)
code_pays_IS02_versioned_data.add_version(Millesime.M2024, CODES_PAYS_ISO2_COG_2024)

CodePaysISO2 = set_format.new(
    "CodePaysISO2", name, description, source, code_pays_IS02_versioned_data
)


name = "Codes ISO3 Pays"
description = "Code ISO 3 de pays pour un Code Officiel Géographique donné"

code_pays_IS03_versioned_data = VersionedSet[Millesime]()
code_pays_IS03_versioned_data.add_version(Millesime.M2023, CODES_PAYS_ISO3_COG_2023)
code_pays_IS03_versioned_data.add_version(Millesime.M2024, CODES_PAYS_ISO3_COG_2024)

CodePaysISO3 = set_format.new(
    "CodePaysISO3", name, description, source, code_pays_IS03_versioned_data
)
