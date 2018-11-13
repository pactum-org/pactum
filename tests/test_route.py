from pactum.route import Route
from pactum.resources import Resource


def test_basic_route(resource):
    route = Route('/test/', resource=resource, methods=[])

    assert route.path == '/test/'
    assert route.resource == resource
    assert len(route.methods) == 0


def test_route_class_definition():
    class TestRoute(Route):
        path = '/test/'
        resource = Resource()
        methods = []

    route = TestRoute()

    assert route.path == '/test/'
    assert isinstance(route.resource, Resource)
    assert len(route.methods) == 0


def test_prefer_parameter_to_class_definition():
    class TestRoute(Route):
        path = '/test/'
        resource = None
        methods = []

    route = TestRoute(
        path="/test_by_param/",
        resource=Resource(),
        methods=['GET']
    )

    assert len(route.methods) == 1
    assert route.path == "/test_by_param/"
    assert isinstance(route.resource, Resource)
