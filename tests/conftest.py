import pytest

from pactum.route import Route
from pactum.version import Version, VersionSelector


@pytest.fixture
def route():
    return Route(path="/resource")


@pytest.fixture
def version(route):
    return Version(
        name="v0",
        selector_option="/v0",
        routes=(
            route,
        ),
    )

