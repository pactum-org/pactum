from unittest.mock import call, MagicMock, Mock

import pytest

from pactum import verbs
from pactum.action import Action
from pactum.route import Route
from pactum.request import Request
from pactum.version import Version


def test_basic_version_with_routes():
    version = Version(
        name="1.0",
        routes=[],
    )

    assert version.name == "1.0"
    assert len(version.routes) == 0


def test_version_class_definition_with_routes():
    class V1(Version):
        name = "V1"
        routes = []

    version = V1()

    assert version.name == "V1"
    assert len(version.routes) == 0


def test_fail_if_no_routes_and_no_version():
    with pytest.raises(TypeError):
        Version(name="v1")


def test_class_def_fails_if_no_routes():
    class V1(Version):
        name = "V1"

    with pytest.raises(TypeError):
        V1()


def test_prefer_parameter_to_class_definition(route):
    class TestVersion(Version):
        name = "Test Version"
        routes = []

    version = TestVersion(
        name="Test Version by parameter",
        routes=[route]
    )

    assert len(version.routes) == 1
    assert version.name == "Test Version by parameter"
    assert version.routes[0].parent == version


def test_validate_ambiguous_routes_on_version_init(resource):
    action1 = Action(Request(verb=verbs.GET), responses=[])
    action2 = Action(Request(verb=verbs.POST), responses=[])
    action3 = Action(Request(verb=verbs.GET), responses=[])
    route1 = Route('/route/', actions=[action1, action2])
    route2 = Route('/route/', actions=[action3])

    class TestVersion(Version):
        name = "v1"
        routes = [route1, route2]

    with pytest.raises(AttributeError):
        TestVersion()


def test_accept_method_calls_visit_and_route_accepts():
    mock_wrapper = Mock()
    mock_wrapper.mocked_visitor = MagicMock()
    mock_wrapper.mocked_route1 = MagicMock()
    mock_wrapper.mocked_route2 = MagicMock()

    version = Version(
        name='v2',
        routes=[mock_wrapper.mocked_route1, mock_wrapper.mocked_route2])
    version.accept(mock_wrapper.mocked_visitor)

    # Assert last 3 calls because of iterations over route on init.
    assert mock_wrapper.mock_calls[-3:] == [
        call.mocked_visitor.visit_version(version),
        call.mocked_route1.accept(mock_wrapper.mocked_visitor),
        call.mocked_route2.accept(mock_wrapper.mocked_visitor)
    ]
