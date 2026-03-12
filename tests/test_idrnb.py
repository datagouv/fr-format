import pytest

from frformat import IdRNB


def test_idrnb_format():
    valid_id = "FT4RKBXBVH9S"

    idrnb = IdRNB()
    assert idrnb.format(valid_id) == valid_id

    for _id in ["FT4R-KBXB-VH9S", "ft4rkbxbvh9s"]:
        with pytest.raises(ValueError):
            idrnb.format(_id)
