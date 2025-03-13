from frformat import set_format
from frformat.formats.code_postal_frozenset import CODES_POSTAUX

name = "Code postal"
description = "Vérifie que le code postal est bien un code postal français. La dernière mise à jour date du 8 février 2025"
source = "https://datanova.laposte.fr/datasets/laposte-hexasmal"

CodePostal = set_format.new("CodePostal", name, description, source, CODES_POSTAUX)
