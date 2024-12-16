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

    # Test empty versioned_set
    assert vs.ls() == []

    assert vs.get_data("2021") is None

    with pytest.raises(ValueError):
        vs.get_data("latest")

    assert vs.add_version(BaseVersion("2025"), frozenset({"Paris"})) is None
    assert vs.add_version(BaseVersion("2024"), frozenset({"Lyon"})) is None
    assert vs.get_data("2025") == frozenset({"Paris"})

    # Duplicate id
    with pytest.raises(ValueError, match="The version id 2024 already exists!"):
        vs.add_version(BaseVersion("2024"), frozenset({"Marseille"}))

    # sorting with version-id
    assert vs.ls() == [BaseVersion("2024"), BaseVersion("2025")]
    assert not vs.ls() == [BaseVersion("2025"), BaseVersion("2024")]

    # "latest" version-id
    assert vs.get_data("latest") == frozenset({"Paris"})

    # Immutable data
    data = vs.get_data("2025")
    with pytest.raises(AttributeError):
        data.add("Nice")

    # non BaseVersion type
    with pytest.raises(AttributeError):
        vs.add_version("1234", frozenset({"Lyon"}))
