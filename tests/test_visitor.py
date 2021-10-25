import pytest

from pactum import (
    API,
    Action,
    ListResource,
    QueryString,
    Request,
    Resource,
    Response,
    Route,
    Version,
    fields,
    verbs,
)
from pactum.base import Element
from pactum.visitor import BaseVisitor


class BlueprintVisitor(BaseVisitor):
    def __init__(self):
        self.blueprints = []

    def visit_api(self, api):
        self.blueprints.append('api visited')

    def visit_version(self, version):
        self.blueprints.append('version visited')

    def visit_route(self, route):
        self.blueprints.append('route visited')

    def visit_action(self, action):
        self.blueprints.append('action visited')

    def visit_querystring(self, querystring):
        self.blueprints.append('querystring visited')

    def visit_request(self, request):
        self.blueprints.append('request visisted')

    def visit_response(self, response):
        self.blueprints.append('response visited')

    def visit_resource(self, resource):
        self.blueprints.append('resource visited')

    def visit_field(self, field):
        self.blueprints.append('field visited')

    def visit_list_resource(self, list_resource):
        self.blueprints.append('list resource visited')


@pytest.fixture
def visitor():
    return BlueprintVisitor()


def test_visitor_api_call(visitor):
    api = API(versions=[Version(name='v1', routes=[])])
    api.accept(visitor)

    assert visitor.blueprints == [
        'api visited',
        'version visited',
    ]


def test_visitor_version_call(visitor):
    version = Version(name='v1', routes=[Route(path='/test')])
    version.accept(visitor)

    assert visitor.blueprints == [
        'version visited',
        'route visited',
    ]


def test_visitor_route_call(visitor):
    route = Route(path='/test', actions=[Action(responses=[])])
    route.accept(visitor)

    assert visitor.blueprints == [
        'route visited',
        'action visited',
    ]


def test_visitor_route_call_with_querystring(visitor):
    route = Route(
        path='/test',
        actions=[Action(responses=[])],
        querystrings=[QueryString(name='test_qs')],
    )
    route.accept(visitor)

    assert visitor.blueprints == [
        'route visited',
        'action visited',
        'querystring visited',
    ]


def test_visitor_action_call(visitor):
    action = Action(request=Request(verb=verbs.GET), responses=[Response(status=200)])
    action.accept(visitor)

    assert visitor.blueprints == [
        'action visited',
        'request visisted',
        'response visited',
    ]


def test_visitor_request_call(visitor):
    request = Request(verb=verbs.GET, payload=Resource())
    request.accept(visitor)

    assert visitor.blueprints == [
        'request visisted',
        'resource visited',
    ]


def test_visitor_response_call(visitor):
    response = Response(status=200, body=Resource())
    response.accept(visitor)

    assert visitor.blueprints == [
        'response visited',
        'resource visited',
    ]


def test_visitor_resource_call(visitor):
    resource = Resource(fields=[fields.Field(name='test')])
    resource.accept(visitor)

    assert visitor.blueprints == [
        'resource visited',
        'field visited',
    ]


def test_visitor_list_resource_call(visitor):
    list_resource = ListResource(resource=Resource())
    list_resource.accept(visitor)

    assert visitor.blueprints == [
        'list resource visited',
        'resource visited',
    ]


def test_visitor_field_call(visitor):
    field = fields.Field(name='test')
    field.accept(visitor)

    assert visitor.blueprints == [
        'field visited',
    ]


def test_visitor_resource_field_call(visitor):
    field = fields.ResourceField(name='test', resource=Resource())
    field.accept(visitor)

    assert visitor.blueprints == [
        'field visited',
        'resource visited',
    ]


def test_visitor_querystring_call(visitor):
    querystring = QueryString()
    querystring.accept(visitor)

    assert visitor.blueprints == [
        'querystring visited',
    ]


@pytest.mark.parametrize(
    'visitor_name',
    [
        'visit_field',
        'visit_api',
        'visit_version',
        'visit_route',
        'visit_action',
        'visit_querystring',
        'visit_request',
        'visit_response',
        'visit_resource',
        'visit_field',
        'visit_list_resource',
    ],
)
def test_abstract_base_visitor(visitor_name):
    visitor = BaseVisitor()
    node = Element()
    with pytest.raises(NotImplementedError):
        getattr(visitor, visitor_name)(node)
