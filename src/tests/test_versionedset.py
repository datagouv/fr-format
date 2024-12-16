from functools import total_ordering

import pytest

from frformat.versioned_set import Version, VersionedSet


def test_versionedset():
    @total_ordering
    class BaseVersion(Version):
        def __init__(self, id: str) -> None:
            self.id = id

        def get_id(self) -> str:
            return self.id

        @classmethod
        def is_sorted(cls) -> bool:
            return True

        def __eq__(self, other):
            return self.id == other.id

        def __lt__(self, other):
            return self.id < other.id
    
    vs = VersionedSet[BaseVersion]()

    with pytest.raises(ValueError):
        vs.get_data("latest")

    assert vs.add_version(BaseVersion("2025"), frozenset({"Paris"})) is None
    assert vs.add_version(BaseVersion("2024"), frozenset({"Lyon"})) is None

    with pytest.raises(ValueError):
        vs.add_version(BaseVersion("2024"), frozenset({"Marseille"}))

    assert vs.ls() == [BaseVersion("2024"), BaseVersion("2025")]
    assert not vs.ls() == [BaseVersion("2025"), BaseVersion("2024")]

    assert vs.get_data("2025") == frozenset({"Paris"})
    assert vs.get_data("2021") is None

    assert vs.get_data("latest") == frozenset({"Paris"})
    assert not vs.get_data("latest") == frozenset({"Lyon"})
