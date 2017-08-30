import pytest

from pactum.route import Route
from pactum.version import Version, version_selector


@pytest.fixture
def route():
    return Route(path="/resource")


@pytest.fixture
def version(route):
    return Version(
        name="v0",
        selector=version_selector("/v0"),
        routes=(
            route,
        ),
    )
