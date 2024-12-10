import pytest
from frformat.versioned_set import BaseVersion, VersionedSet


def test_versionedset ():

    vs = VersionedSet[BaseVersion]()

    assert vs.add_version(BaseVersion("2025"), frozenset({"Paris"})) is None  # ok
    assert vs.add_version(BaseVersion("2024"), frozenset({"Lyon"})) is None  # ok
    
    with pytest.raises(ValueError):
        vs.add_version(BaseVersion("2024"), frozenset({"Marseille"}))  # not ok
