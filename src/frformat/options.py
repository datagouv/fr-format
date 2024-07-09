from dataclasses import dataclass, field


@dataclass
class Options:
    """
       The class Options is used to represent a list of options to validate a French format.

    Attributes:
        ignore_case: Boolean
            Indicates if case should be ignored.
            When set to True, all characters in the string will be converted to lowercase.

        ignore_accents: Boolean
            Indicates if accents should be ignored.
            When set to True, characters with accents will be replaced with their non-accented counterparts.
            Example: 'à' will be replaced by 'a'.

        replace_non_alphanumeric_with_space: Boolean
            Indicates if non-alphanumeric characters should be ignored.
            When set to True, punctuation marks and symbols will be replaced by a space.

        ignore_extra_whitespace: Boolean
            Indicates if extra white space should be ignored.
            When set to True, multiple consecutive spaces will be treated as a single space, and leading or trailing spaces will be removed.

        extra_valid_values: set of string
            A collection of additional valid values.
            This set includes any extra values that should be considered valid during the validation process, beyond the original set of valid values.
            This allows for customized validation rules to accommodate special cases or exceptions.
    """

    ignore_case: bool = False
    ignore_accents: bool = False
    replace_non_alphanumeric_with_space: bool = False
    ignore_extra_whitespace: bool = False
    extra_valid_values: set = field(default_factory=set)
