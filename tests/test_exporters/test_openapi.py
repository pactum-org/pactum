from pactum import Action, API, Request, Route, Version, verbs
from copy import copy
from pactum.exporters.openapi import OpenAPIV3Exporter


def test_openapi_exporter_initialization():
    exporter = OpenAPIV3Exporter()
    assert exporter.result['openapi'] == OpenAPIV3Exporter.OPENAPI_VERSION
    assert exporter.result['servers'] == []
    assert exporter.result['info'] == {}
    assert exporter.result['paths'] == {}
    assert exporter.result['components'] == {'schemas': {}}
    assert exporter.result['security'] == {}
    assert exporter.result['tags'] == {}


def test_visit_api_for_api_with_versions_overrides_versions():
    exporter = OpenAPIV3Exporter()
    v1 = Version(name='v1', routes=[])
    v2 = Version(name='v2', routes=[])
    api = API(
        name='Test API', versions=[v1, v2],
        description='API for tests.'
    )

    exporter.visit_api(api)

    assert exporter.result['info']['title'] == 'Test API'
    assert exporter.result['info']['description'] == 'API for tests.'
    assert exporter.result['info']['termsOfService'] == ''
    assert exporter.result['info']['contact'] == {}
    assert exporter.result['info']['license'] == {}
    assert exporter.result['info']['version'] == 'v2'
    assert api.versions == [v2]


def test_visit_version_does_nothing_to_openapi_spec():
    exporter = OpenAPIV3Exporter()
    result = copy(exporter.result)
    version = Version(name='v1', routes=[])

    exporter.visit_version(version)

    assert exporter.result == result


def test_visit_route_sets_specs_paths():
    exporter = OpenAPIV3Exporter()
    route = Route(path='/test-path/', description='Route for tests.')
    exporter.visit_route(route)
    paths = exporter.result['paths']
    assert '/test-path/' in paths
    assert paths['/test-path/']['summary'] == ''
    assert paths['/test-path/']['description'] == 'Route for tests.'
    assert paths['/test-path/']['servers'] == []
    assert paths['/test-path/']['parameters'] == {}


def test_visit_action_populates_paths_verbs():
    exporter = OpenAPIV3Exporter()
    route = Route(path='/test-path/', description='Route for tests.')
    request = Request(verb=verbs.GET)
    action = Action(request=request, responses=[], description='Testing action')
    action.parent = route

    exporter.result['paths'] = {'/test-path/': {}}

    exporter.visit_action(action)

    assert 'get' in exporter.result['paths']['/test-path/']
    parsed_action = exporter.result['paths']['/test-path/']['get']
    assert parsed_action['description'] == 'Testing action'
    assert parsed_action['summary'] == 'Testing action'
    assert parsed_action['operationId'] == 'TestingAction'
    assert parsed_action['deprecated'] is False

    assert parsed_action['tags'] == []
    assert parsed_action['externalDocs'] == []
    assert parsed_action['parameters'] == []
    assert parsed_action['responses'] == {}
    assert parsed_action['callbacks'] == []
    assert parsed_action['security'] == {}
    assert parsed_action['servers'] == {}
