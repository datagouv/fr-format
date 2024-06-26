from frformat import enum_format

DEPARTEMENTS_SET = (
    {str(x).zfill(2) for x in range(1, 20)}
    | {"2A", "2B", "984", "986", "987", "988", "989"}
    | {str(x) for x in range(21, 96)}
    | {str(x) for x in range(971, 979)}
)

name = "Numéro du département"
description = "Vérifie que le numéro de département correspond bien à un numéro de département français"

NumeroDepartement = enum_format.new(
    "NumeroDepartement", name, description, DEPARTEMENTS_SET
)
