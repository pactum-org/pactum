import pytest

from pactum import API, Route, Version
from pactum.version import version_selector


@pytest.fixture
def route():
    return Route(path="/resource", methods=[])


@pytest.fixture
def version(route):
    return Version(
        name="v0",
        selector=version_selector("/v0"),
        routes=(
            route,
        ),
    )


@pytest.fixture
def api():
    api = API(
        name="Test API",
        versions=[],
    )
    return api
