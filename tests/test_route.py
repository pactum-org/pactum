import pytest

from pactum.route import Route


def test_basic_route():
    route = Route('/test/', methods=[])

    assert route.path == '/test/'
    assert len(route.methods) == 0


def test_route_class_definition():
    class TestRoute(Route):
        path = '/test/'
        methods = []

    route = TestRoute()

    assert route.path == '/test/'
    assert len(route.methods) == 0


def test_prefer_parameter_to_class_definition():
    class TestRoute(Route):
        path = '/test/'
        methods = []

    route = TestRoute(
        path="/test_by_param/",
        methods=['GET']
    )

    assert len(route.methods) == 1
    assert route.path == "/test_by_param/"


def test_fail_route_with_no_path(resource):
    with pytest.raises(TypeError):
        Route(methods=[])
