from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar, Union

from frformat.formatter import DefaultFormatter, Formatter


@dataclass
class Metadata:
    name: str
    description: str


ValueType = TypeVar("ValueType", str, float, int, contravariant=True)


class CustomFormat(ABC, Generic[ValueType]):
    metadata: Metadata
    formatter: Formatter = DefaultFormatter[ValueType]()

    @classmethod
    @abstractmethod
    def is_valid(cls, value: ValueType) -> bool:
        ...

    @classmethod
    def format(cls, value: ValueType) -> str:
        if not cls.is_valid(value):
            raise ValueError(f"{cls.metadata.name} is not valid")
        return cls.formatter.format(value)


CustomStrFormat = CustomFormat[str]
CustomNumericFormat = CustomFormat[Union[float, int]]
