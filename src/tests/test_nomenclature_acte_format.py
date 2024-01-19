from frformat.nomenclature_acte_format import AUTHORIZED_VALUES, NomenclatureActe


def test_nomenclature_acte_value():
    acte_value = "Fonction publique/foobar"
    assert NomenclatureActe.is_valid(acte_value)

    test_cases = ["foobar", "Fonction publique /foobar" "Fonction publique"]
    for tc in test_cases:
        assert not NomenclatureActe.is_valid(tc)


def test_is_valid_with_details():
    valid_prefix = AUTHORIZED_VALUES[0]
    invalid_prefix = "invalid"
    test_cases = [
        {
            "value": f"{valid_prefix}/blabla",
            "expected": (True, None),
        },
        {
            "value": f"{valid_prefix} blabla",
            "expected": (False, ["le signe oblique « / » est manquant"]),
        },
        {
            "value": f"{valid_prefix} /blabla",
            "expected": (
                False,
                ["le signe oblique ne doit pas être précédé ni suivi d'espace"],
            ),
        },
        {
            "value": f"{valid_prefix}/ blabla",
            "expected": (
                False,
                ["le signe oblique ne doit pas être précédé ni suivi d'espace"],
            ),
        },
        {
            "value": f"{invalid_prefix}/ blabla",
            "expected": (
                False,
                [
                    "le signe oblique ne doit pas être précédé ni suivi d'espace",
                    f"le préfixe de nomenclature Actes '{invalid_prefix}' n'est pas reconnu",
                ],
            ),
        },
        {
            "value": f"{invalid_prefix}/blabla",
            "expected": (
                False,
                [
                    f"le préfixe de nomenclature Actes '{invalid_prefix}' n'est pas reconnu"
                ],
            ),
        },
    ]

    for tc in test_cases:
        assert NomenclatureActe.is_valid_with_details(tc["value"]) == tc["expected"]
