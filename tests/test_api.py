import pytest

from pactum.api import API
from pactum.exceptions import SpecificationWarning
from version import Version, version_selector


def test_base_api(version):
    api = API(
        name="Test API",
        versions=(
            version,
        ),
    )

    assert api.name == "Test API"
    assert len(api.versions) == 1
    assert api.validate()


def test_warning_api_with_different_selectors(version, route):
    other_version = Version(
        name="2.0",
        selector=version_selector("application/vnd.test.v2+json"),
        routes=(
            route,
        ),
    )

    api = API(
        name="Test API",
        versions=(
            version,
            other_version,
        )
    )

    with pytest.warns(SpecificationWarning):
        api.validate()


def test_warning_api_with_no_version():
    with pytest.warns(SpecificationWarning):
        api = API(
            name="Test API",
            versions=(),
        )
        api.validate()


# noinspection PyArgumentList
def test_error_positional_args(version):
    with pytest.raises(TypeError):
        API("Name", (version,))
