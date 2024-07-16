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

    @abstractmethod
    def is_valid(self, value: ValueType) -> bool:
        ...

    def format(self, value: ValueType) -> str:
        if not self.is_valid(value):
            raise ValueError(f"{self.metadata.name} is not valid")
        return self.formatter.format(value)


CustomStrFormat = CustomFormat[str]
CustomNumericFormat = CustomFormat[Union[float, int]]
