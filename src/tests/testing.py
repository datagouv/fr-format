from typing import List


def validation_test_helper_factory(Class):
    def aux_test_helper(
        test_cases: List[str], isStrict: bool, expectValid: bool
    ) -> None:
        adjective = "strictly" if isStrict else "leniently"
        validKeywoard = "valid" if expectValid else "invalid"

        for tc in test_cases:
            assert (
                Class.is_valid(tc, strict=isStrict) == expectValid
            ), f"Check that departement { tc } is { adjective } { validKeywoard }"

    return aux_test_helper
