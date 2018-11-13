import pytest

from pactum.api import API
from pactum.resources import Resource
from pactum.route import Route
from pactum.version import Version


@pytest.fixture
def route():
    return Route('/test/')


@pytest.fixture
def version(route):
    return Version(
        name="v0",
        routes=[
            route,
        ],
    )


@pytest.fixture
def api():
    api = API(
        name="Test API",
        versions=[],
    )
    return api


@pytest.fixture
def resource():
    return Resource()
