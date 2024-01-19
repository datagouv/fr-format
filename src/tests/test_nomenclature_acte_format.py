from frformat import NomenclatureActe


def test_nomenclature_acte_value():
    acte_value = "Fonction publique/foobar"
    assert NomenclatureActe.is_valid(acte_value)

    test_cases = ["foobar", "Fonction publique /foobar" "Fonction publique"]
    for tc in test_cases:
        assert not NomenclatureActe.is_valid(tc)
