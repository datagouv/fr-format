from frformat import set_format
from frformat.formats.code_postal_frozenset import CODES_POSTAUX_SEMESTRE1_2025
from frformat.versioned_set import VersionedSet
from frformat.versions import Semestre

name = "Code postal"
description = "Vérifie que le code postal est bien un code postal français pour un semestre bien déterminé donné"
source = "https://datanova.laposte.fr/datasets/laposte-hexasmal"
last_update = "08/01/2025"

code_postal_versioned_data = VersionedSet[Semestre]()
code_postal_versioned_data.add_version(Semestre.S1_2025, CODES_POSTAUX_SEMESTRE1_2025)
CodePostal = set_format.new(
    "CodePostal", name, description, source, code_postal_versioned_data
)
