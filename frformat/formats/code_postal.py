from frformat import set_format
from frformat.formats.code_postal_frozenset import CODES_POSTAUX_SEMESTRE1_2025

name = "Code postal"
description = "Code postal français. La dernière mise à jour date du 8 février 2025"
source = "https://datanova.laposte.fr/datasets/laposte-hexasmal"

CodePostal = set_format.new("CodePostal", name, description, source, CODES_POSTAUX_SEMESTRE1_2025)
