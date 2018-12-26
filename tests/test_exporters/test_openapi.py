import pytest
from copy import copy

from pactum import Action, API, fields
from pactum import ListResource, Querystring
from pactum import Resource, Response, Request, Route
from pactum import Version, verbs
from pactum.exporters.openapi import NotSpecified, OpenAPIV3Exporter


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


def test_visit_action_populates_paths_verbs_with_parameters():
    exporter = OpenAPIV3Exporter()
    route = Route(path='/test-path/{code}', description='Route for tests.')
    request = Request(verb=verbs.GET)
    action = Action(request=request, responses=[], description='Testing action')
    action.parent = route

    exporter.result['paths'] = {'/test-path/{code}': {}}

    exporter.visit_action(action)

    assert 'get' in exporter.result['paths']['/test-path/{code}']
    parsed_action = exporter.result['paths']['/test-path/{code}']['get']
    assert parsed_action['description'] == 'Testing action'
    assert parsed_action['summary'] == 'Testing action'
    assert parsed_action['operationId'] == 'TestingAction'
    assert parsed_action['deprecated'] is False

    assert parsed_action['tags'] == []
    assert parsed_action['externalDocs'] == []
    assert len(parsed_action['parameters']) == 1
    assert parsed_action['parameters'][0] == {
        'name': 'code',
        'in': 'path',
        'required': True
    }
    assert parsed_action['responses'] == {}
    assert parsed_action['callbacks'] == []
    assert parsed_action['security'] == {}
    assert parsed_action['servers'] == {}


def test_visit_action_populates_queries_with_route_qs():
    exporter = OpenAPIV3Exporter()
    querystring = Querystring(name='limit', type=fields.IntegerField)
    route = Route(path='/test-path', querystrings=[querystring])
    request = Request(verb=verbs.GET)
    action = Action(request=request, responses=[], description='Testing action')
    action.parent = route

    exporter.result['paths'] = {'/test-path': {}}

    exporter.visit_action(action)

    assert 'get' in exporter.result['paths']['/test-path']
    parsed_action = exporter.result['paths']['/test-path']['get']

    assert len(parsed_action['parameters']) == 1
    assert parsed_action['parameters'][0] == {
        'name': 'limit',
        'in': 'query',
        'required': False,
        'schema': {'type': 'integer'},
        'description': ''
    }


def test_visit_request_populates_requestBody_with_payload_reference(resource):

    exporter = OpenAPIV3Exporter()
    route = Route(path='/test-path/')
    request = Request(verb=verbs.GET, payload=resource)
    action = Action(request=request, responses=[])
    action.parent = route

    exporter.result['paths'] = {
        '/test-path/': {'get': {}}
    }

    exporter.visit_request(request)

    parsed_action = exporter.result['paths']['/test-path/']['get']
    assert 'schema' in parsed_action['requestBody']
    assert parsed_action['requestBody']['schema']['$ref'] == '#/components/schemas/Resource'


def test_visit_response_appends_response_objects_to_path(resource):
    exporter = OpenAPIV3Exporter()
    route = Route(path='/test-path/')
    request = Request(verb=verbs.GET)
    response = Response(
        status=200, description='Response for testing',
        headers=[('content-type', 'application/json')],
        body=resource
    )
    action = Action(
        request=request, responses=[response]
    )
    action.parent = route

    exporter.result['paths'] = {
        '/test-path/': {'get': {'responses': {}}}
    }

    exporter.visit_response(response)

    parsed_responses = exporter.result['paths']['/test-path/']['get']['responses']
    assert '200' in parsed_responses
    expected_schema = {'schema': {'$ref': '#/components/schemas/Resource'}}
    assert parsed_responses['200']['content']['application/json'] == expected_schema
    assert parsed_responses['200']['headers'] == {}


def test_visit_resource_populates_schemas_component(resource):
    exporter = OpenAPIV3Exporter()

    exporter.visit_resource(resource)

    assert 'Resource' in exporter.result['components']['schemas']
    resource = exporter.result['components']['schemas']['Resource']
    assert resource['type'] == 'object'
    assert resource['required'] == []
    assert resource['properties'] == {}


def test_visit_resource_populates_required_fields():
    class TestResource(Resource):
        fields = [fields.IntegerField(name='code', required=True)]

    exporter = OpenAPIV3Exporter()
    exporter.visit_resource(TestResource())
    assert 'TestResource' in exporter.result['components']['schemas']
    schema = exporter.result['components']['schemas']['TestResource']
    assert schema['type'] == 'object'
    assert schema['required'] == ['code']
    assert schema['properties'] == {}


def test_visit_list_resource_populates_schemas_with_array_and_ref():
    class TestResource(Resource):
        pass

    class TestListResource(ListResource):
        resource = TestResource()

    exporter = OpenAPIV3Exporter()
    exporter.visit_list_resource(TestListResource())

    assert 'TestListResource' in exporter.result['components']['schemas']

    schema = exporter.result['components']['schemas']['TestListResource']
    assert schema['type'] == 'array'
    assert schema['items'] == {'$ref': '#/components/schemas/TestResource'}


def test_visit_field_populates_component_schema_with_field_type():
    code_field = fields.IntegerField(name='code', required=True)

    class TestResource(Resource):
        fields = [code_field]

    TestResource()

    exporter = OpenAPIV3Exporter()
    exporter.result['components']['schemas'] = {
        'TestResource': {'properties': {}}
    }

    exporter.visit_field(code_field)

    properties = exporter.result['components']['schemas']['TestResource']['properties']
    assert 'code' in properties
    assert properties['code']['type'] == 'integer'


def test_resource_field_visit_populated_with_resource_reference():
    class OtherResource(Resource):
        pass

    resource_field = fields.ResourceField(name='other_resource', resource=OtherResource())

    class TestResource(Resource):
        fields = [resource_field]

    TestResource()

    exporter = OpenAPIV3Exporter()
    exporter.result['components']['schemas'] = {
        'TestResource': {'properties': {}}
    }

    exporter.visit_field(resource_field)

    properties = exporter.result['components']['schemas']['TestResource']['properties']
    assert 'other_resource' in properties
    assert properties['other_resource'] == {'$ref': '#/components/schemas/OtherResource'}


def test_custom_field_with_extension():
    class CustomField(fields.Field):
        extensions = {'openapi.type': 'custom'}
    custom_field = CustomField(name='test_name')

    class TestResource(Resource):
        fields = [custom_field]

    TestResource()

    exporter = OpenAPIV3Exporter()
    exporter.result['components']['schemas'] = {
        'TestResource': {'properties': {}}
    }
    exporter.visit_field(custom_field)

    properties = exporter.result['components']['schemas']['TestResource']['properties']
    assert 'test_name' in properties
    assert properties['test_name']['type'] == 'custom'


def test_visit_for_custom_field_without_extension_raises_error():
    class CustomField(fields.Field):
        pass
    custom_field = CustomField()

    class TestResource(Resource):
        fields = [custom_field]

    TestResource()
    exporter = OpenAPIV3Exporter()
    exporter.result['components']['schemas'] = {
        'TestResource': {'properties': {}}
    }

    with pytest.raises(NotSpecified):
        exporter.visit_field(custom_field)
