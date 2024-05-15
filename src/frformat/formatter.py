from typing import Protocol


class Formatter(Protocol):
    def format(self, value: str) -> str:
        ...


class DefaultFormatter:
    def format(self, value: str) -> str:
        return value
