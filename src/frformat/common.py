import re

USPACE = "\u00A0"  # Unbreakable space
UTSPACE = "\u202F"  # Unbreakable thin space


def normalize_text(val: str) -> str:
    val = val.lower()
    val = val.replace("-", " ")
    val = val.replace("_", " ")
    val = val.replace("'", " ")
    val = val.replace(",", " ")
    val = val.replace("  ", " ")
    val = re.sub(r"[èéêë]", "e", val)
    val = re.sub(r"[àáâãäå]", "a", val)
    val = re.sub(r"[ìíîï]", "i", val)
    val = re.sub(r"[òóôõö]", "o", val)
    val = re.sub(r"[ùúûü]", "u", val)
    return val
