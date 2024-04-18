from abc import ABC, abstractmethod
from typing import Protocol


class CustomFormatProtocol(Protocol):
    @classmethod
    def name(cls) -> str:
        """
        Human-readable name
        """
        ...

    @classmethod
    def description(cls) -> str:
        ...

    @classmethod
    def is_valid(cls, value: str) -> bool:
        ...

    @classmethod
    def format(cls, value: str) -> str:
        """Returns value in standard format

        Expects the value to be valid, otherwise raises an `InvalidValueError`
        """
        ...


class WithMetadata(ABC):
    @classmethod
    @abstractmethod
    def name(cls) -> str:
        ...

    @classmethod
    @abstractmethod
    def description(cls) -> str:
        ...


class CustomFormat(CustomFormatProtocol, WithMetadata, ABC):
    @classmethod
    @abstractmethod
    def is_valid(cls, value: str) -> bool:
        ...

    @classmethod
    def format(cls, value: str) -> str:
        if not cls.is_valid(value):
            raise ValueError(f"{cls.name()} is not valid")
        return cls._format(value)

    @classmethod
    def _format(cls, value: str) -> str:
        # Specify the default behaviour
        return value
