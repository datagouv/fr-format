from typing import List

from frformat.geo_enum_format import Millesime
from frformat.options import Options


def validation_test_helper_factory(Class):
    def test_helper(
        test_cases: List[str], expectValid: bool, cog: Millesime, options: Options
    ) -> None:
        if options == Options():
            adjective = "strictly"
        else:
            adjective = "leniently"

        validKeywoard = "valid" if expectValid else "invalid"

        for tc in test_cases:
            assert (
                Class(cog, options).is_valid(tc) == expectValid
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
        optionsTrue = Options(
            ignore_case=True,
            ignore_accents=True,
            replace_non_alphanumeric_with_space=True,
            ignore_extra_whitespace=True,
        )
        all_cogs = [Millesime.A2023, Millesime.A2024]

        for cog in all_cogs:
            _test_class(strict_test_cases, expectValid=True, cog=cog, options=Options())
            _test_class(
                lenient_test_cases,
                expectValid=False,
                cog=cog,
                options=Options(),
            )
            _test_class(
                invalid_test_cases,
                expectValid=False,
                cog=cog,
                options=Options(),
            )

            _test_class(
                strict_test_cases,
                expectValid=True,
                cog=cog,
                options=optionsTrue,
            )
            _test_class(
                lenient_test_cases,
                expectValid=True,
                cog=cog,
                options=optionsTrue,
            )
            _test_class(
                invalid_test_cases,
                expectValid=False,
                cog=cog,
                options=optionsTrue,
            )

    return test_helper
