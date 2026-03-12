import re

from frformat.options import Options

NBSP = "\u00a0"  # Non-breaking space
NNBSP = "\u202f"  # Narrow non-breaking space


def normalize_value(val: str, options: Options) -> str:
    if options.ignore_case is True:
        val = val.lower()

    if options.ignore_accents is True:
        val = _replace_accented_letters(val)

    if options.replace_non_alphanumeric_with_space is True:
        val = re.sub(r"[^a-zA-Z0-9]", " ", val)

    if options.ignore_extra_whitespace is True:
        val = val.strip()
        val = re.sub(r"[\s]+", " ", val)
    return val


def _replace_accented_letters(val: str) -> str:
    val = re.sub(r"[èéêë]", "e", val)
    val = re.sub(r"[àáâãäå]", "a", val)
    val = re.sub(r"[ìíîï]", "i", val)
    val = re.sub(r"[òóôõö]", "o", val)
    val = re.sub(r"[ùúûü]", "u", val)
    val = re.sub(r"[ÈÉÊË]", "E", val)
    val = re.sub(r"[ÀÁÂÃÄÅ]", "A", val)
    val = re.sub(r"[ÌÍÎÏ]", "I", val)
    val = re.sub(r"[ÒÓÔÕÖ]", "O", val)
    val = re.sub(r"[ÙÚÛÜ]", "U", val)

    return val
