import warnings

from contract.base import Element
from contract.exceptions import SpecificationWarning


class API(Element):
    def __init__(self, *, name, version_selector, versions, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.version_selector = version_selector
        self.versions = versions

    def validate(self):
        for version in self.versions:
            version.validate()

        if not self.versions:
            warnings.warn("API does not specifies at least one version", SpecificationWarning)

        return super().validate()
