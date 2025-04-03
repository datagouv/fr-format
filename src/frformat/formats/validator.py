from frformat import set_format
from frformat.get_values_script import get_valid_values
from frformat.versioned_set import VersionedSet
from frformat.versions import Millesime

name = "Nom de validateur"
description = "Vérification si la valeur donnée est bien valide selon des valeurs valides récupérées"
source = "source1"

validator_versioned_data = VersionedSet[Millesime]()

valid_values = get_valid_values(
    "https://www.insee.fr/fr/statistiques/fichier/8377162/v_commune_2025.csv", "COM"
)
validator_versioned_data.add_version(Millesime.M2023, valid_values)


Validator = set_format.new(
    "Validator", name, description, source, validator_versioned_data
)
