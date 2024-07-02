import re

from frformat.options import Options

NBSP = "\u00A0"  # Non-breaking space
NNBSP = "\u202F"  # Narrow non-breaking space


def normalize_value(val: str, options: Options) -> str:
    if options.ignore_case is True:
        val = val.lower()

    if options.ignore_non_alphanumeric is True:
        val = re.sub(r"[^a-zA-Z0-9]", " ", val)

    if options.ignore_extra_white_space is True:
        val = val.strip()
        val = val.replace("  ", " ")

    if options.ignore_accents is True:
        val = re.sub(r"[èéêë]", "e", val)
        val = re.sub(r"[àáâãäå]", "a", val)
        val = re.sub(r"[ìíîï]", "i", val)
        val = re.sub(r"[òóôõö]", "o", val)
        val = re.sub(r"[ùúûü]", "u", val)

    return val
