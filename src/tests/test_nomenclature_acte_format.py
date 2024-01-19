from frformat import NomenclatureActe


def test_nomenclature_acte_value():
    acte_value = "Fonction publique/foobar"
    assert NomenclatureActe.is_valid(acte_value)

    test_cases = ["foobar", "Fonction publique /foobar" "Fonction publique"]
    for tc in test_cases:
        assert not NomenclatureActe.is_valid(tc)


def test_is_valid_with_details():
    test_cases = [
        {
            "value": "Commande publique/blabla",
            "expected": (True, None),
        },
        {
            "value": "Commande publique blabla",
            "expected": (False, "le signe oblique « / » est manquant"),
        },
        {
            "value": "Commande publique /blabla",
            "expected": (
                False,
                "le signe oblique ne doit pas être précédé ni suivi d'espace",
            ),
        },
        {
            "value": "Commande publique/ blabla",
            "expected": (
                False,
                "le signe oblique ne doit pas être précédé ni suivi d'espace",
            ),
        },
        {
            "value": "Cmd publique/blabla",
            "expected": (
                False,
                "le préfixe de nomenclature Actes 'Cmd publique' n'est pas reconnu",
            ),
        },
    ]

    for tc in test_cases:
        assert NomenclatureActe.is_valid_with_details(tc["value"]) == tc["expected"]
