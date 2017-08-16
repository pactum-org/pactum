from contract.base import Element
from contract.exceptions import InvalidVersionSelector


class API(Element):
    def __init__(self, name, versions, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.versions = versions

    def validate(self):
        if len(self.versions) == 1:
            return

        last_version = None
        for version in self.versions:
            if last_version is not None and last_version.selector != version.selector:
                raise InvalidVersionSelector(f"Different selectors for versions in {version} and {last_version}")
            last_version = version
            version.validate()
