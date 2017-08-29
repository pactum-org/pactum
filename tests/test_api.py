import pytest

from contract.api import API
from contract.exceptions import SpecificationWarning
from contract.version import VersionSelector


def test_base_api(version):
    api = API(
        name="Test API",
        version_selector=VersionSelector.PATH,
        versions=(
            version,
        ),
    )

    assert api.name == "Test API"
    assert len(api.versions) == 1
    assert api.validate()


def test_warning_api_with_no_version():
    with pytest.warns(SpecificationWarning):
        api = API(
            name="Test API",
            version_selector=VersionSelector.PATH,
            versions=(),
        )
        api.validate()


# noinspection PyArgumentList
def test_error_positional_args(version):
    with pytest.raises(TypeError):
        API("Name", VersionSelector.PATH, (version,))
