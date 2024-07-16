from frformat.nomenclature_acte_format import (
    AUTHORIZED_VALUES,
    EXTRA_SPACE,
    INVALID_PREFIX,
    MISSING_SLASH,
    NomenclatureActe,
)


def test_is_valid_with_details():
    valid_prefix = next(iter(AUTHORIZED_VALUES))
    invalid_prefix = "invalid"
    test_cases = [
        {
            "value": f"{valid_prefix}/blabla",
            "expected_is_valid": True,
            "expected_details": None,
        },
        {
            "value": f"{valid_prefix} blabla",
            "expected_is_valid": False,
            "expected_details": [MISSING_SLASH],
        },
        {
            "value": f"{valid_prefix} /blabla",
            "expected_is_valid": False,
            "expected_details": [EXTRA_SPACE],
        },
        {
            "value": f"{valid_prefix}/ blabla",
            "expected_is_valid": False,
            "expected_details": [EXTRA_SPACE],
        },
        {
            "value": f"{invalid_prefix}/ blabla",
            "expected_is_valid": False,
            "expected_details": [EXTRA_SPACE, INVALID_PREFIX(invalid_prefix)],
        },
        {
            "value": f"{invalid_prefix}/blabla",
            "expected_is_valid": False,
            "expected_details": [INVALID_PREFIX(invalid_prefix)],
        },
    ]

    nomenclature_acte = NomenclatureActe()
    for tc in test_cases:
        assert nomenclature_acte.is_valid(tc["value"]) == tc["expected_is_valid"]
        assert nomenclature_acte.is_valid_with_details(tc["value"]) == (
            tc["expected_is_valid"],
            tc["expected_details"],
        )
