import pytest

from frformat.versioned_set import BaseVersion, VersionedSet


def test_versionedset():
    vs = VersionedSet[BaseVersion]()
    assert vs.get_data("latest") is None