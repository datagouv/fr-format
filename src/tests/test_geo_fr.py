from frformat import (
    CodeCommuneInsee,
    CodePostal,
    Commune,
    Departement,
    NumeroDepartement,
    Pays,
    Region,
)
from tests.testing import strict_lenient_test_helper_factory


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


def test_pays():
    _test_pays = strict_lenient_test_helper_factory(Pays)

    pays_strict = ["France", "Pays-Bas", "Bosnie-Herzégovine"]
    pays_lenient = ["france", "Pays Bas", "bosnie herzegovine"]
    pays_invalid = ["L'Eldorado", "Zubrowska"]

    _test_pays(pays_strict, pays_lenient, pays_invalid)
