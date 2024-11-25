from frformat.geo_enum_format import Millesime


def test_is_latest():
    recent_millesime_name = max(member.name for member in Millesime)
    recent_millesime = Millesime[recent_millesime_name]

    assert (
        Millesime.LATEST == recent_millesime
    ), "LATEST is not the most recent available Millesime"
