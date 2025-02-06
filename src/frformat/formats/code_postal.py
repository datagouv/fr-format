from frformat import set_format
from frformat.formats.code_postal_frozenset import CODES_POSTAUX_SEMESTRE1_2025

name = "Code postal"
description = "Vérifie que le code postal est bien un code postal français pour une version/semestre bien déterminée donnée"
source = "https://datanova.laposte.fr/datasets/laposte-hexasmal"

CodePostal = set_format.new(
    "CodePostal", name, description, source, CODES_POSTAUX_SEMESTRE1_2025
)
