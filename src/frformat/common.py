import re

from frformat.options import Options

NBSP = "\u00A0"  # Non-breaking space
NNBSP = "\u202F"  # Narrow non-breaking space


def normalize_text(val: str, option_items: Options) -> str:
    if option_items.ignore_case is True:
        val = val.lower()

    if option_items.ignore_punctuation is True:
        val = val.replace(",", " ")
        val = val.replace("-", " ")

    if option_items.ignore_underscore is True:
        val = val.replace("_", " ")

    if option_items.ignore_fullwidth_apostrophe is True:
        val = val.replace("'", " ")

    if option_items.ignore_space is True:
        val = val.replace("  ", " ")

    if option_items.ignore_accents is True:
        val = re.sub(r"[èéêë]", "e", val)
        val = re.sub(r"[àáâãäå]", "a", val)
        val = re.sub(r"[ìíîï]", "i", val)
        val = re.sub(r"[òóôõö]", "o", val)
        val = re.sub(r"[ùúûü]", "u", val)

    return val
