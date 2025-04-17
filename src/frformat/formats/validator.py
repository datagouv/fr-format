from frformat import set_format
from frformat.get_values import get_values_from_csv
from frformat.infra_file_reader import LocalReader, RemoteReader
from frformat.versioned_set import VersionedSet
from frformat.versions import Millesime

name = "Nom de validateur"
description = "Vérification si la valeur donnée est bien valide selon des valeurs valides récupérées"
source = "source1"

validator_versioned_data = VersionedSet[Millesime]()
remote_reader = RemoteReader()
local_reader = LocalReader()

valid_values_2023 = get_values_from_csv(
    "src/tests/test_files_data/values.csv", "Username", remote_reader, local_reader
)
validator_versioned_data.add_version(Millesime.M2023, valid_values_2023)


Validator = set_format.new(
    "Validator", name, description, source, validator_versioned_data
)
