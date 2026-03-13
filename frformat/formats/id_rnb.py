from .. import CustomStrFormat, Metadata

name = "ID-RNB"
description = "Check ID-RNB validity (from Référentiel National des Bâtiments), but does not check if the id exists."
source = "https://github.com/fab-geocommuns/RNB-coeur/blob/main/app/batid/services/rnb_id.py"


class IdRNB(CustomStrFormat):
    metadata = Metadata(name, description, source)

    def is_valid(self, value: str) -> bool:
        return len(value) == 12 and all(c in "123456789ABCDEFGHJKMNPQRSTVWXYZ" for c in value)
