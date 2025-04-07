from frformat import set_format
from frformat.get_values_script import get_valid_values
from frformat.set_format import INSEE_SOURCE
from frformat.versioned_set import VersionedSet
from frformat.versions import Millesime

name = "Nom de canton"
description = "Vérifie que le nom de canton est un canton ou pseudo-canton français valide pour un Code Officiel Géographique donné"
source = INSEE_SOURCE

canton_versioned_data = VersionedSet[Millesime]()
canton_values_2023 = get_valid_values(
    "https://www.insee.fr/fr/statistiques/fichier/6800675/v_canton_2023.csv", "LIBELLE"
)
canton_versioned_data.add_version(Millesime.M2023, canton_values_2023)

canton_values_2024 = get_valid_values(
    "https://www.insee.fr/fr/statistiques/fichier/7766585/v_canton_2024.csv", "LIBELLE"
)
canton_versioned_data.add_version(Millesime.M2024, canton_values_2024)

Canton = set_format.new("Canton", name, description, source, canton_versioned_data)
