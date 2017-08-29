class PactumError(Exception):
    pass


class PactumWarning(Warning):
    pass


class SpecificationWarning(PactumWarning):
    pass


class InvalidVersionSelector(PactumError):
    pass
