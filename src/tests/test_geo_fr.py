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
    NumeroDepartement,
    Pays,
    Region,
)
from tests.testing import (
    strict_lenient_test_helper_factory,
    validation_test_helper_factory,
)


def test_code_fantoir():
    _test_fantoir = validation_test_helper_factory(CodeFantoir)

    fantoir_valid = ["ZB03A"]
    fantoir_invalid = ["1000"]

    _test_fantoir(fantoir_valid, True)
    _test_fantoir(fantoir_invalid, False)


def test_code_commune_insee():
    value = "01015"
    assert CodeCommuneInsee.is_valid(value)
    assert CodeCommuneInsee.format(value) == value

    assert CodeCommuneInsee.is_valid("2B002")
    assert not CodeCommuneInsee.is_valid("77777")


def test_code_postal():
    value = "05560"
    assert CodePostal.is_valid(value)
    assert CodePostal.format(value) == value

    assert not CodePostal.is_valid("77777")
    assert not CodePostal.is_valid("2B002")


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


def test_latitude_l93():
    assert LatitudeL93.is_valid(44.2)
    # À vérifier
    assert LatitudeL93.is_valid(42)
    assert not LatitudeL93.is_valid(55)


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
    region_lenient = [
        "Centre Val de Loire",
        "La Reunion",
        "corse",
        "bfc",
        "BFC",
        "aura",
    ]
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
