from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol

from frformat.formatter import DefaultFormatter, Formatter


@dataclass
class Metadata:
    name: str
    description: str


class CustomStrFormat(ABC):
    metadata: Metadata
    formatter: Formatter = DefaultFormatter()

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

    @classmethod
    @abstractmethod
    def is_valid(cls, value: float) -> bool:
        ...

    @classmethod
    def format(cls, value: float) -> str:
        if not cls.is_valid(value):
            raise ValueError(f"{cls.metadata.name} is not valid")
        return cls._format(value)

    @classmethod
    def _format(cls, value: float) -> str:
        # Specify the default behaviour
        return str(value)
