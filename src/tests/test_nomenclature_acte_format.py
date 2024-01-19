from frformat.nomenclature_acte_format import AUTHORIZED_VALUES, EXTRA_SPACE, INVALID_PREFIX, NomenclatureActe, MISSING_SLASH


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
            "expected": (False, [MISSING_SLASH]),
        },
        {
            "value": f"{valid_prefix} /blabla",
            "expected": (
                False,
                [EXTRA_SPACE],
            ),
        },
        {
            "value": f"{valid_prefix}/ blabla",
            "expected": (
                False,
                [EXTRA_SPACE],
            ),
        },
        {
            "value": f"{invalid_prefix}/ blabla",
            "expected": (
                False,
                [
                    EXTRA_SPACE,
                    INVALID_PREFIX(invalid_prefix)                
                ],
            ),
        },
        {
            "value": f"{invalid_prefix}/blabla",
            "expected": (
                False,
                [
                    INVALID_PREFIX(invalid_prefix)
                ],
            ),
        },
    ]

    for tc in test_cases:
        assert NomenclatureActe.is_valid_with_details(tc["value"]) == tc["expected"]
