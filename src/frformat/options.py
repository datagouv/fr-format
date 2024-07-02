from dataclasses import dataclass


@dataclass
class Options:
    ignore_case: bool = False
    ignore_non_alphanumeric: bool = False
    ignore_extra_white_space: bool = False
    ignore_accents: bool = False
    extra_valid_value: set[str] = set()
