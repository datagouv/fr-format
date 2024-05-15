from abc import ABC, abstractmethod
from dataclasses import dataclass

from frformat.formatter import DefaultFormatter, Formatter


@dataclass
class Metadata:
    name: str
    description: str


class CustomStrFormat(ABC):
    metadata: Metadata
    formatter: Formatter = DefaultFormatter[str]()

    @classmethod
    @abstractmethod
    def is_valid(cls, value: str) -> bool:
        ...

    @classmethod
    def format(cls, value: str) -> str:
        if not cls.is_valid(value):
            raise ValueError(f"{cls.metadata.name} is not valid")
        return cls.formatter.format(value)


class CustomFloatFormat(ABC):
    metadata: Metadata
    formatter: Formatter = DefaultFormatter[float]()

    @classmethod
    @abstractmethod
    def is_valid(cls, value: float) -> bool:
        ...

    @classmethod
    def format(cls, value: float) -> str:
        if not cls.is_valid(value):
            raise ValueError(f"{cls.metadata.name} is not valid")
        return cls.formatter.format(value)
