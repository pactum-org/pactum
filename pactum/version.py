import warnings

from pactum.base import Element
from pactum.exceptions import SpecificationWarning, SpecificationError


class VersionSelector:
    type = None

    def __init__(self, selector):
        self.selector = selector

    def validate(self):
        raise NotImplementedError("Must be implemented in subclass")


class PathVersionSelector(VersionSelector):
    type = "path"

    def validate(self):
        if not self.selector.startswith("/"):
            raise SpecificationError("PathVersionSelector must start with '/'")
        return True


class AcceptHeaderVersionSelector(VersionSelector):
    type = "accept_header"

    def validate(self):
        if "/" not in self.selector:
            raise SpecificationError("Invalid MIME type selector: missing type/subtype separator")

        if not self.selector.islower():
            raise SpecificationError("Invalid MIME type selector: uppercase characters")

        type_, subtype = self.selector.split("/", 1)

        if type_ != "application":
            warnings.warn("It's recommended to use 'application' MIME type", SpecificationWarning)

        if not subtype.startswith("vnd."):
            warnings.warn("Vendor-specific MIME subtypes should starts with 'vnd.'", SpecificationWarning)

        return True


class CustomHeaderVersionSelector(VersionSelector):
    type = "custom_header"

    def __init__(self, *selector):
        selector = ": ".join(selector)
        super().__init__(selector)

    def validate(self):
        if ": " not in self.selector:
            raise SpecificationError("Invalid HTTP Header: not in format 'X-Header: value'")

        if not self.selector.startswith("X-"):
            warnings.warn("It's recommended that custom headers starts with 'X-' prefix", SpecificationWarning)

        return True


def version_selector(selector):
    if selector.startswith("/"):
        return PathVersionSelector(selector)
    elif "/" in selector:
        return AcceptHeaderVersionSelector(selector)
    elif selector.startswith("X-"):
        return CustomHeaderVersionSelector(selector)
    else:
        raise SpecificationError("Invalid selector: {}".format(selector))


class Version(Element):
    def __init__(self, *, name=None, selector=None, routes=None, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.selector = selector
        self.routes = routes

    def validate(self):
        if not self.routes:
            warnings.warn("Version does not specifies at least one route", SpecificationWarning)

        self.selector.validate()

        return super().validate()
