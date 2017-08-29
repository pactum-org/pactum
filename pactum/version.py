import warnings
from enum import IntFlag

from pactum.base import Element
from pactum.exceptions import SpecificationWarning


class VersionSelector(IntFlag):
    PATH = 1
    ACCEPT_HEADER = 2
    CUSTOM_HEADER = 4


class Version(Element):
    def __init__(self, *, name, selector_option, routes, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.selector_option = selector_option
        self.routes = routes

    def validate(self):
        if not isinstance(self.selector_option, str) and not self.selector_option[0].lower().startswith("x-"):
            warnings.warn("Custom HTTP header shoud starts with 'X-'", SpecificationWarning)

        if not self.routes:
            warnings.warn("Version does not specifies at least one route", SpecificationWarning)

        return super().validate()
