from typing import Dict, FrozenSet

from frformat import geo_enum_format
from frformat.geo.code_pays_frozenset import (
    CODE_PAYS_ISO2_FROZEN_SET_COG_2023,
    CODE_PAYS_ISO2_FROZEN_SET_COG_2024,
    CODE_PAYS_ISO3_FROZEN_SET_COG_2023,
    CODE_PAYS_ISO3_FROZEN_SET_COG_2024,
)
from frformat.geo_enum_format import Millesime

name = "Codes ISO2 Pays"
description = "Code ISO 2 de pays pour un Code Officiel Géographique donné"

all_cog_versions: Dict[Millesime, FrozenSet[str]] = {
    Millesime.A2023: CODE_PAYS_ISO2_FROZEN_SET_COG_2023,
    Millesime.A2024: CODE_PAYS_ISO2_FROZEN_SET_COG_2024,
}

CodePaysISO2 = geo_enum_format.new("CodePaysISO2", name, description, all_cog_versions)

name = "Codes ISO3 Pays"
description = "Code ISO 3 de pays pour un Code Officiel Géographique donné"

all_cog_versions: Dict[Millesime, FrozenSet[str]] = {
    Millesime.A2023: CODE_PAYS_ISO3_FROZEN_SET_COG_2023,
    Millesime.A2024: CODE_PAYS_ISO3_FROZEN_SET_COG_2024,
}

CodePaysISO3 = geo_enum_format.new("CodePaysISO3", name, description, all_cog_versions)
