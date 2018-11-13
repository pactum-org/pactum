import pytest

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


def test_append_route(route):
    version = Version(
        name="1.0",
        routes=[],
    )

    version.append(route)
    assert len(version.routes) == 1


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
