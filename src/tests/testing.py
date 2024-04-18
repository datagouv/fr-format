from typing import List


def validation_test_helper_factory(Class):
    def test_helper(test_cases: List[str], isStrict: bool, expectValid: bool) -> None:
        adjective = "strictly" if isStrict else "leniently"
        validKeywoard = "valid" if expectValid else "invalid"

        for tc in test_cases:
            assert (
                Class.is_valid(tc, strict=isStrict) == expectValid
            ), f"Check that departement { tc } is { adjective } { validKeywoard }"

    return test_helper


def strict_lenient_test_helper_factory(Class):
    """Returns a test_helper function, to which can be provided strict test
    cases, exclusively lenient test cases, and invalid test cases, for a given
    class"""
    _test_class = validation_test_helper_factory(Class)

    def test_helper(
        strict_test_cases: List[str],
        lenient_test_cases: List[str],
        invalid_test_cases: List[str],
    ) -> None:
        _test_class(strict_test_cases, isStrict=True, expectValid=True)
        _test_class(lenient_test_cases, isStrict=True, expectValid=False)
        _test_class(invalid_test_cases, isStrict=True, expectValid=False)

        _test_class(strict_test_cases, isStrict=False, expectValid=True)
        _test_class(lenient_test_cases, isStrict=False, expectValid=True)
        _test_class(invalid_test_cases, isStrict=False, expectValid=False)

    return test_helper
