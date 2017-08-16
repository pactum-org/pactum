import warnings
from enum import IntFlag

from contract.base import Element
from contract.exceptions import SpecificationWarning


class VersionSelector(IntFlag):
    PATH = 1
    ACCEPT_HEADER = 2
    CUSTOM_HEADER = 4


class Version(Element):
    def __init__(self, name, selector, endpoints,
                 path=None, accept=None, custom_header=None, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.endpoints = endpoints
        self.selector = selector
        self.path = path if selector == VersionSelector.PATH else None
        self.accept = accept if selector == VersionSelector.ACCEPT_HEADER else None
        self.custom_header = custom_header if selector == VersionSelector.CUSTOM_HEADER else None

    def validate(self):
        if self.custom_header and not self.custom_header[0].lower().startswith("X-"):
            warnings.warn("Custom HTTP header shoud starts with 'X-'", SpecificationWarning)

        # noinspection PyTypeChecker
        if len([s for s in VersionSelector if (self.selector & s) != s]) < len(VersionSelector):
            warnings.warn("Multiple selectors cause ambiguous behaviours", SpecificationWarning)
