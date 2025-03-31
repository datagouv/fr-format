from enum import Enum
from functools import total_ordering


@total_ordering
class Millesime(Enum):
    """Millesime class implements the `Version` protocol methods."""

    M2015 = "2015"
    M2016 = "2016"
    M2017 = "2017"
    M2018 = "2018"
    M2019 = "2019"
    M2020 = "2020"
    M2021 = "2021"
    M2022 = "2022"
    M2023 = "2023"
    M2024 = "2024"
    LATEST = "latest"

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def __lt__(self, other) -> bool:
        return self.value < other.value

    def get_id(self) -> str:
        return self.value

    @classmethod
    def is_sorted(cls) -> bool:
        return True
