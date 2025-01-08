from functools import total_ordering

import pytest

from frformat.versioned_set import VersionedSet


@total_ordering
class SortedVersion:
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


class NonSortedVersion:
    def __init__(self, id: str) -> None:
        self.id = id

    def get_id(self) -> str:
        return self.id

    @classmethod
    def is_sorted(cls) -> bool:
        return False


vs = VersionedSet[SortedVersion]()


def test_empty_behaviour():
    assert vs.ls() == []

    assert vs.get_data("2021") is None

    assert vs.get_data("latest") is None


def test_with_data():
    vs.add_version(SortedVersion("2025"), frozenset({"Paris"}))
    vs.add_version(SortedVersion("2024"), frozenset({"Lyon"}))

    with pytest.raises(ValueError, match="The version id 2024 already exists!"):
        vs.add_version(SortedVersion("2024"), frozenset({"Marseille"}))

    assert vs.ls() == [SortedVersion("2024"), SortedVersion("2025")]

    assert vs.get_data("2025") == frozenset({"Paris"})

    assert vs.get_data("latest") == frozenset({"Paris"})

    with pytest.raises(AttributeError):
        vs.add_version("1234", frozenset({"Lyon"}))  # type: ignore


def test_non_sortable_version():
    v = VersionedSet[NonSortedVersion]()
    v.add_version(NonSortedVersion("2021"), frozenset({"Nice"}))
    v.add_version(NonSortedVersion("2020"), frozenset({"Jura"}))

    assert v.get_data("latest") is None
