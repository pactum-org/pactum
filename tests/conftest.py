import pytest

from pactum import verbs
from pactum.action import Action
from pactum.api import API
from pactum.querystring import QueryString
from pactum.request import Request
from pactum.resources import Resource
from pactum.response import Response
from pactum.route import Route
from pactum.version import Version


@pytest.fixture
def route(resource):
    return Route(path='/test/')


@pytest.fixture
def version(route):
    return Version(
        name='v0',
        routes=[
            route,
        ],
    )


@pytest.fixture
def api():
    api = API(
        name='Test API',
        versions=[],
    )
    return api


@pytest.fixture
def resource():
    return Resource()


@pytest.fixture
def request_():  # `request` is a pytest reserved fixture.
    return Request(verb=verbs.GET)


@pytest.fixture
def response():
    return Response(status=200, body='')


@pytest.fixture
def action(request_, response):
    return Action(request=request_, responses=[response])


@pytest.fixture
def querystring():
    return QueryString(name='test_querystring')
