class Options:
    def __init__(
        self,
        ignore_case,
        ignore_punctuation,
        ignore_underscore,
        ignore_fullwidth_apostrophe,
        ignore_space,
        ignore_accents: bool,
    ):
        self.ignore_case = ignore_case
        self.ignore_punctuation = ignore_punctuation
        self.ignore_underscore = ignore_underscore
        self.ignore_fullwidth_apostrophe = ignore_fullwidth_apostrophe
        self.ignore_space = ignore_space
        self.ignore_accents = ignore_accents
