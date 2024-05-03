from abc import ABC, abstractmethod


class WithMetadata(ABC):
    @classmethod
    @abstractmethod
    def name(cls) -> str:
        """ Human-readable name """
        ...

    @classmethod
    @abstractmethod
    def description(cls) -> str:
        ...

class CustomStrFormat(WithMetadata, ABC):
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

class CustomFloatFormat(WithMetadata, ABC):
    @classmethod
    @abstractmethod
    def is_valid(cls, value: float) -> bool:
        ...

    @classmethod
    def format(cls, value: float) -> str:
        if not cls.is_valid(value):
            raise ValueError(f"{cls.name()} is not valid")
        return cls._format(value)

    @classmethod
    def _format(cls, value: float) -> str:
        # Specify the default behaviour
        return str(value)

