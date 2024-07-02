from dataclasses import dataclass, field


@dataclass
class Options:
    ignore_case: bool = False
    ignore_non_alphanumeric: bool = False
    ignore_extra_white_space: bool = False
    ignore_accents: bool = False
    extra_valid_values: set = field(default_factory=set)
