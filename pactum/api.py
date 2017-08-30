import warnings

from pactum.base import Element
from pactum.exceptions import SpecificationWarning


class API(Element):
    def __init__(self, *, name, versions, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.versions = versions

    def validate(self):
        if not self.versions:
            warnings.warn("API does not specifies at least one version", SpecificationWarning)

        last_version = None
        for version in self.versions:
            if last_version and version.selector.type != last_version.selector.type:
                warnings.warn(f"Ambiguous version selector for version {last_version} and {version}", SpecificationWarning)

            version.validate()

            last_version = version

        return super().validate()
