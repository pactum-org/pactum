import pytest

from contract.exceptions import SpecificationWarning
from contract.version import Version, VersionSelector


def test_warning_version_with_path_and_accept():
    with pytest.warns(SpecificationWarning):
        version = Version(
            name="1.0",
            selector=VersionSelector.PATH | VersionSelector.ACCEPT_HEADER,
            path="/v1",
            accept="application/vnd.test.v1+json",
            endpoints=[],
        )
        version.validate()


def test_warning_custom_header_with_no_x_prefix():
    with pytest.warns(SpecificationWarning):
        version = Version(
            name="1.0",
            selector=VersionSelector.CUSTOM_HEADER,
            custom_header=("API-Version", "1.0"),
            endpoints=[],
        )
        version.validate()
