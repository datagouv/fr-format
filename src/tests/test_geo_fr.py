from frformat import (
    Canton,
    CodeCommuneInsee,
    CodeFantoir,
    CodePaysISO2,
    CodePaysISO3,
    CodePostal,
    CodeRegion,
    Commune,
    Departement,
    LatitudeL93,
    LongitudeL93,
    NumeroDepartement,
    Pays,
    Region,
)
from frformat.common import NBSP, NNBSP
from tests.testing import strict_lenient_test_helper_factory


def test_code_fantoir():
    fantoir_valid = "ZB03A"
    fantoir_invalid = "1000"
    code_fantoir = CodeFantoir()
    assert code_fantoir.is_valid(fantoir_valid)
    assert not code_fantoir.is_valid(fantoir_invalid)


def test_code_commune_insee():
    value = "01015"
    code_commune_insee = CodeCommuneInsee()
    assert code_commune_insee.is_valid(value)
    assert code_commune_insee.format(value) == value

    assert code_commune_insee.is_valid("2B002")
    assert not code_commune_insee.is_valid("77777")


def test_code_postal():
    value = "05560"
    code_postal = CodePostal()
    assert code_postal.is_valid(value)
    assert code_postal.format(value) == value

    assert not code_postal.is_valid("77777")
    assert not code_postal.is_valid("2B002")


def test_commune():
    _test_commune = strict_lenient_test_helper_factory(Commune)

    commune_strict = ["Bellac", "Le Dorat", "Petite-Île", "L'Isle-Adam"]
    commune_lenient = ["bellac", "le dorat", "Petite-Ile", "l'isle adam"]
    commune_invalid = ["Costa del Sol"]

    _test_commune(commune_strict, commune_lenient, commune_invalid)


def test_canton():
    _test_canton = strict_lenient_test_helper_factory(Canton)

    canton_strict = ["Saint-Pierre-1"]
    canton_lenient = ["le tampon", "saint andre"]
    canton_invalid = ["Neuchâtel"]

    _test_canton(canton_strict, canton_lenient, canton_invalid)


def test_departement():
    _test_departement = strict_lenient_test_helper_factory(Departement)

    departement_strict = ["Alpes-Maritimes", "Gard", "Mayotte", "Vendée"]
    departement_lenient = [
        "Alpes Maritimes",
        "gard",
        "Vendee",
    ]
    departement_invalid = ["Charente-Inférieure"]

    _test_departement(departement_strict, departement_lenient, departement_invalid)


def test_longitude_l93():
    longitudel93 = LongitudeL93()
    assert longitudel93.format(224234) == "224" + NNBSP + "234" + NBSP + "m"
    assert longitudel93.format(224234.0) == "224" + NNBSP + "234,00" + NBSP + "m"

    invalid_test_cases = [-435522.3, -554234, 2076524, 5436780.23]

    for tc in invalid_test_cases:
        assert not longitudel93.is_valid(tc)

    valid_test_cases = [0, 1234546, 1234546.32, -123554, -234.546]

    for tc in valid_test_cases:
        assert longitudel93.is_valid(tc)


def test_latitude_l93():
    latitudel93 = LatitudeL93()
    assert (
        latitudel93.format(6757121) == "6" + NNBSP + "757" + NNBSP + "121" + NBSP + "m"
    )
    assert (
        latitudel93.format(6757121.337)
        == "6" + NNBSP + "757" + NNBSP + "121,34" + NBSP + "m"
    )

    assert latitudel93.is_valid(6544234.2)
    assert latitudel93.is_valid(7145278)

    invalid_test_cases = [0, -6145765.9, -7234567, 7233478, 6000658.5]

    for tc in invalid_test_cases:
        assert not latitudel93.is_valid(tc)


def test_numero_departement():
    _test_num_departement = strict_lenient_test_helper_factory(NumeroDepartement)

    num_departement_strict = ["05", "2B", "974"]
    num_departement_lenient = ["2a", "2b"]
    num_departement_invalid = ["99", "051"]

    _test_num_departement(
        num_departement_strict,
        num_departement_lenient,
        num_departement_invalid,
    )


def test_region():
    _test_region = strict_lenient_test_helper_factory(Region)

    region_strict = ["Centre-Val de Loire", "La Réunion", "Corse"]
    region_lenient = ["Centre Val de Loire", "La Reunion", "corse"]
    region_invalid = ["Beleriand", "Canyon Cosmo"]

    _test_region(region_strict, region_lenient, region_invalid)


def test_code_region():
    _test_code_region = strict_lenient_test_helper_factory(CodeRegion)

    code_region_strict = ["01", "75"]
    code_region_lenient = []
    code_region_invalid = ["AA", "00"]

    _test_code_region(code_region_strict, code_region_lenient, code_region_invalid)


def test_pays():
    _test_pays = strict_lenient_test_helper_factory(Pays)

    pays_strict = ["France", "Pays-Bas", "Bosnie-Herzégovine"]
    pays_lenient = ["france", "Pays Bas", "bosnie herzegovine"]
    pays_invalid = ["L'Eldorado", "Zubrowska"]

    _test_pays(pays_strict, pays_lenient, pays_invalid)


def test_code_pays():
    _test_iso2 = strict_lenient_test_helper_factory(CodePaysISO2)

    iso2_strict = ["FR", "JP"]
    iso2_lenient = ["Fr", "jp"]
    iso2_invalid = ["AA", "FRA"]

    _test_iso2(iso2_strict, iso2_lenient, iso2_invalid)

    _test_iso3 = strict_lenient_test_helper_factory(CodePaysISO3)

    iso3_strict = ["FRA", "JPN"]
    iso3_lenient = ["Fra", "jpn"]
    iso3_invalid = ["AAA", "FR"]

    _test_iso3(iso3_strict, iso3_lenient, iso3_invalid)
