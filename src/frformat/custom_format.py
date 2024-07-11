from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar, Union

from frformat.common import Options
from frformat.formatter import DefaultFormatter, Formatter


@dataclass
class Metadata:
    name: str
    description: str


ValueType = TypeVar("ValueType", str, float, int, contravariant=True)


class CustomFormat(ABC, Generic[ValueType]):
    metadata: Metadata
    formatter: Formatter = DefaultFormatter[ValueType]()

    def __init__(self, options: Options):
        self.options = options

    @abstractmethod
    def is_valid(self, value: ValueType) -> bool:
        ...

    @classmethod
    def format(cls, value: ValueType) -> str:
        instance = cls(Options())
        if not instance.is_valid(value):
            raise ValueError(f"{cls.metadata.name} is not valid")
        return cls.formatter.format(value)


CustomStrFormat = CustomFormat[str]
CustomNumericFormat = CustomFormat[Union[float, int]]
