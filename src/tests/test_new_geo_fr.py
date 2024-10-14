from frformat import CodeRegion, Region
from tests.new_testing import strict_lenient_test_helper_factory


def test_code_region():
    _test_code_region = strict_lenient_test_helper_factory(CodeRegion)

    code_region_strict = ["01", "75"]
    code_region_lenient = []
    code_region_invalid = ["AA", "00"]

    _test_code_region(code_region_strict, code_region_lenient, code_region_invalid)


def test_region():
    _test_region = strict_lenient_test_helper_factory(Region)

    region_strict = ["Centre-Val de Loire", "La Réunion", "Corse"]
    region_lenient = ["Centre Val de Loire", "La Reunion", "corse"]
    region_invalid = ["Beleriand", "Canyon Cosmo"]

    _test_region(region_strict, region_lenient, region_invalid)
