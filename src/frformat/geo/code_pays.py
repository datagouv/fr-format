from typing import Dict, Set

from frformat import geo_enum_format
from frformat.geo.code_pays_set import (
    CODE_PAYS_ISO2_SET_COG_2023,
    CODE_PAYS_ISO2_SET_COG_2024,
    CODE_PAYS_ISO3_SET_COG_2023,
    CODE_PAYS_ISO3_SET_COG_2024,
)
from frformat.geo_enum_format import Millesime

name = "Codes ISO2 Pays"
description = "Code ISO 2 de pays selon COG2023 et COG2024"

all_cog_versions: Dict[Millesime, Set[str]] = {
    Millesime.A2023: CODE_PAYS_ISO2_SET_COG_2023,
    Millesime.A2024: CODE_PAYS_ISO2_SET_COG_2024,
}

CodePaysISO2 = geo_enum_format.new("CodePaysISO2", name, description, all_cog_versions)

name = "Codes ISO3 Pays"
description = "Code ISO 3 de pays selon COG2023 et COG2024"

all_cog_versions: Dict[Millesime, Set[str]] = {
    Millesime.A2023: CODE_PAYS_ISO3_SET_COG_2023,
    Millesime.A2024: CODE_PAYS_ISO3_SET_COG_2024,
}

CodePaysISO3 = geo_enum_format.new("CodePaysISO3", name, description, all_cog_versions)
