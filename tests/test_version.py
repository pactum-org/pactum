import pytest

from pactum.exceptions import SpecificationWarning
from pactum.version import Version, VersionSelector


def test_basic_version(route):
    version = Version(
        name="v1",
        selector_option="/v1",
        routes=(
            route,
        )
    )
    version.validate()


def test_warning_custom_header_with_no_x_prefix(route):
    with pytest.warns(SpecificationWarning):
        version = Version(
            name="v1",
            selector_option=("API-Version", "1.0"),
            routes=(
                route
            ),
        )
        version.validate()


def test_warning_version_no_route():
    with pytest.warns(SpecificationWarning):
        version = Version(
            name="v1",
            selector_option="v1",
            routes=(),
        )
        version.validate()


# noinspection PyArgumentList
def test_error_positional_args():
    with pytest.raises(TypeError):
        Version("Name", VersionSelector.PATH, "/v1")
