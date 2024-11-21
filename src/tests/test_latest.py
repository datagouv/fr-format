from frformat.geo_enum_format import Millesime


def test_is_latest():
    last_millesime_name = ""
    for member in Millesime:
        if member.name > last_millesime_name:
            last_millesime_name = member.name

    last_millesime = Millesime[last_millesime_name]

    assert Millesime.LATEST == last_millesime, "LATEST is not the most recent Millesime"
