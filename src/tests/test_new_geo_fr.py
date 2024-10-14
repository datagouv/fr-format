from frformat import CodeRegion
from tests.new_testing import strict_lenient_test_helper_factory


def test_code_region():
    _test_code_region = strict_lenient_test_helper_factory(CodeRegion)

    code_region_strict = ["01", "75"]
    code_region_lenient = []
    code_region_invalid = ["AA", "00"]

    _test_code_region(code_region_strict, code_region_lenient, code_region_invalid)
