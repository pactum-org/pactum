import pytest

from pactum.exceptions import SpecificationWarning, SpecificationError
from pactum.version import Version, PathVersionSelector, VersionSelector, AcceptHeaderVersionSelector, \
    CustomHeaderVersionSelector, version_selector


def test_basic_version(route):
    version = Version(
        name="v1",
        selector=PathVersionSelector("/v1"),
        routes=(
            route,
        )
    )
    version.validate()


def test_warning_version_no_route():
    with pytest.warns(SpecificationWarning):
        version = Version(
            name="v1",
            selector=PathVersionSelector("/v1"),
            routes=(),
        )
        version.validate()


# noinspection PyArgumentList
def test_error_positional_args(route):
    with pytest.raises(TypeError):
        Version("Name", PathVersionSelector("/v1"), (route,))


# Version Selector
def test_error_validate_abstract_class():
    with pytest.raises(NotImplementedError):
        VersionSelector("").validate()


def test_basic_path_version_selector():
    vs = PathVersionSelector("/v1")
    assert vs.selector == "/v1"
    assert vs.validate()


def test_error_path_version_selector_not_started_slash():
    with pytest.raises(SpecificationError):
        PathVersionSelector("v1").validate()


def test_basic_accept_version_selector():
    vs = AcceptHeaderVersionSelector("application/vnd.test.v2+json")
    assert vs.selector == "application/vnd.test.v2+json"
    assert vs.validate()


def test_error_invalid_accept_version_selector():
    with pytest.raises(SpecificationError):
        AcceptHeaderVersionSelector("invalid").validate()

    with pytest.raises(SpecificationError):
        AcceptHeaderVersionSelector("application/vnd.UPPERCASE.v2+json").validate()


def test_warning_bad_mime_type_accept_version_selector():
    with pytest.warns(SpecificationWarning):
        AcceptHeaderVersionSelector("text/vnd.test.v2+json").validate()

    with pytest.warns(SpecificationWarning):
        AcceptHeaderVersionSelector("application/test.subtype+json").validate()


def test_basic_custom_header_version_selector():
    vs = CustomHeaderVersionSelector("X-API-Version: 1.0")
    assert vs.selector == "X-API-Version: 1.0"
    assert vs.validate()


def test_basic_custom_header_version_selector_tuple():
    vs = CustomHeaderVersionSelector("X-API-Version", "1.0")
    assert vs.selector == "X-API-Version: 1.0"


def test_error_invalid_custom_header_version_selector():
    with pytest.raises(SpecificationError):
        CustomHeaderVersionSelector("Invalid:header").validate()


def test_warning_bad_custom_header_version_selector():
    with pytest.warns(SpecificationWarning):
        CustomHeaderVersionSelector("API-Version: 1.0").validate()


def test_version_selector_helper():
    assert isinstance(version_selector("/v1"), PathVersionSelector)
    assert isinstance(version_selector("application/vnd.test.v2+json"), AcceptHeaderVersionSelector)
    assert isinstance(version_selector("X-API-Version: 1.0"), CustomHeaderVersionSelector)


def test_error_version_selector_helper():
    with pytest.raises(SpecificationError):
        version_selector("invalid")
