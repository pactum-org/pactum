class ContractError(Exception):
    pass


class ContractWarning(Warning):
    pass


class SpecificationWarning(ContractWarning):
    pass


class InvalidVersionSelector(ContractError):
    pass
