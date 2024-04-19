from typing import List


def validation_test_helper_factory(Class):
    def test_helper(test_cases: List[str], expectValid: bool, **kwargs) -> None:
        isStrict = kwargs["strict"] if "strict" in kwargs else None

        if isStrict:
            adjective = "strictly"
        elif isStrict is False:
            adjective = "leniently"
        else:
            adjective = ""

        validKeywoard = "valid" if expectValid else "invalid"

        for tc in test_cases:
            assert (
                Class.is_valid(tc, **kwargs) == expectValid
            ), f"Check that { Class.__name__ } { tc } is { adjective } { validKeywoard }"

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
        _test_class(strict_test_cases, expectValid=True, strict=True)
        _test_class(lenient_test_cases, expectValid=False, strict=True)
        _test_class(invalid_test_cases, expectValid=False, strict=True)

        _test_class(strict_test_cases, expectValid=True, strict=False)
        _test_class(lenient_test_cases, expectValid=True, strict=False)
        _test_class(invalid_test_cases, expectValid=False, strict=False)

    return test_helper
