import locale
from typing import Generic, Protocol, TypeVar, Union

from frformat.common import NBSP

ValueType = TypeVar("ValueType", str, float, int, contravariant=True)


class Formatter(Protocol, Generic[ValueType]):
    def format(self, value: ValueType) -> str:
        ...


class DefaultFormatter(Generic[ValueType]):
    def format(self, value: ValueType) -> str:
        formatted: str = str(value)

        if isinstance(value, float) or isinstance(value, int):
            formatted = _format_with_french_locale(value)

        return formatted


class UnitFormatter(Formatter[float]):
    def __init__(self, unit: str = ""):
        self.unit = unit

    def format(self, value: float) -> str:
        formatted_float = DefaultFormatter[float]().format(value)
        return formatted_float + NBSP + self.unit


def _format_with_french_locale(value: Union[float, int]) -> str:
    format: str = ""
    if isinstance(value, float):
        format = "%.2f"
    if isinstance(value, int):
        format = "%d"
    locale.setlocale(locale.LC_ALL, "fr_FR.UTF-8")
    return locale.format_string(format, value, True)
