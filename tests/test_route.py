import pytest

from pactum.route import Route


def test_basic_route():
    route = Route('/test/', actions=[])

    assert route.path == '/test/'
    assert len(route.actions) == 0
    assert route.parameters == []


def test_route_class_definition():
    class TestRoute(Route):
        path = '/test/'
        actions = []

    route = TestRoute()

    assert route.path == '/test/'
    assert len(route.actions) == 0
    assert route.parameters == []


def test_prefer_parameter_to_class_definition(action):
    class TestRoute(Route):
        path = '/test/'
        actions = []

    route = TestRoute(
        path="/test_by_param/",
        actions=[action]
    )

    assert len(route.actions) == 1
    assert route.path == "/test_by_param/"
    assert route.actions[0].parent == route


def test_fail_route_with_no_path(resource):
    with pytest.raises(TypeError):
        Route(actions=[])


def test_route_with_parameters():
    route = Route('/test/{test-id}', actions=[])

    assert route.path == '/test/{test-id}'
    assert route.parameters == ['test-id']


def test_route_with_multiple_parameters():
    route = Route('/test/{test_id}/{test.slug}/{test-uuid}', actions=[])

    assert route.path == '/test/{test_id}/{test.slug}/{test-uuid}'
    assert route.parameters == ['test_id', 'test.slug', 'test-uuid']


def test_route_with_querystrings(querystring):
    route = Route('/test/', querystrings=[querystring])
    assert route.path == '/test/'
    assert len(route.querystrings) == 1


def test_class_defined_route_with_querystrings(querystring):
    class TestRoute(Route):
        path = '/test/'
        querystrings = [querystring]

    route = TestRoute()
    assert route.path == '/test/'
    assert len(route.querystrings) == 1
