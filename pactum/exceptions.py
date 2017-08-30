class PactumError(Exception):
    pass


class PactumWarning(Warning):
    pass


class SpecificationWarning(PactumWarning):
    pass


class SpecificationError(PactumError):
    pass


class InvalidVersionSelector(SpecificationError):
    pass
