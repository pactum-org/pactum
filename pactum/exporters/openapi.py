from pactum import fields
from pactum.resources import Resource
from pactum.visitor import BaseVisitor

FIELD_TYPES_MAP = {
    fields.IntegerField: 'integer',
    fields.PositiveIntegerField: 'integer',
    fields.StringField: 'string',
    fields.TimestampField: 'datetime',
}


class NotSpecified(Exception):
    pass


class OpenAPIV3Exporter(BaseVisitor):
    """
    Exporter based on OpenAPI specification version 3.0.1.
    https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.1.md
    """

    OPENAPI_VERSION = '3.0.1'

    def __init__(self):
        self.result = {
            'openapi': self.__class__.OPENAPI_VERSION,  # REQUIRED
            'servers': [],
            'info': {},  # REQUIRED
            'paths': {},  # REQUIRED
            'components': {'schemas': {}},
            'security': {},
            'tags': {},
        }

    def visit_api(self, api):
        last_version = api.versions[-1]
        self.result['info'] = {
            'title': api.name,  # REQUIRED
            'description': api.__doc__,
            'termsOfService': '',
            'contact': {},
            'license': {},
            'version': last_version.name,  # REQUIRED
        }
        api.versions = [last_version]  # Versions override to visitonly children for last version.

    def visit_version(self, version):
        pass

    def visit_route(self, route):
        self.result['paths'][route.path] = {
            'summary': '',
            'description': route.__doc__,
            'servers': [],
            # get, put, post, delete, options, head, patch and trace will be populated on children visits.
        }

    def visit_querystring(self, querystring):
        pass

    def visit_action(self, action):
        result = self.result['paths'][action.parent.path][action.request.verb.lower()] = {
            'description': action.__doc__,
            'tags': [],
            'summary': action.__doc__,
            'externalDocs': [],
            'operationId': ''.join(x.title() for x in action.__doc__.split()),
            'parameters': [],
            'responses': {},  # will be populated on children visits.
            'callbacks': [],
            'deprecated': False,
            'security': {},
            'servers': {},
        }
        parameters = action.parent.parameters
        for parameter in parameters:
            param_dict = self._parameter_to_dict(action, parameter)
            result['parameters'].append(param_dict)

        querystrings = action.parent.querystrings
        for qs in querystrings:
            qs_dict = self._querystring_to_dict(qs)
            result['parameters'].append(qs_dict)

    def _parameter_to_dict(self, action, parameter):
        param_dict = {'name': parameter, 'in': 'path', 'required': True}
        success_responses = [
            response
            for response in action.responses
            if str(response.status).startswith('20') and isinstance(response.body, Resource)
        ]
        if success_responses and isinstance(success_responses[0].body, Resource):
            response = success_responses[0]
            resource = response.body
            field = resource[parameter]
            param_dict['schema'] = {'$ref': f'#/components/schemas/{resource.name}/properties/{field.name}'}

        return param_dict

    def _querystring_to_dict(self, querystring):
        qs_dict = {
            'name': querystring.name,
            'in': 'query',
            'required': querystring.required,
            'description': querystring.__doc__,
        }
        if issubclass(querystring.type, fields.Field):
            qs_dict['schema'] = {'type': self._map_field_type(querystring)}
        return qs_dict

    def visit_request(self, request):
        payload = {}
        if request.payload:
            payload = {'schema': {'$ref': f'#/components/schemas/{request.payload.name}'}}
        self.result['paths'][request.parent.parent.path][request.verb.lower()]['requestBody'] = payload

    def visit_response(self, response):
        method = self.result['paths'][response.parent.parent.path][response.parent.request.verb.lower()]
        parsed_response = {
            'description': response.__doc__,
            'links': {},
            'content': {},
        }

        headers = dict(response.headers)
        content_type = headers.pop('content-type', None)
        parsed_response['headers'] = headers

        if content_type is None:
            content_type = 'application/json'

        if response.body:
            parsed_response['content'][content_type] = {
                'schema': {'$ref': f'#/components/schemas/{response.body.name}'}
            }
        method['responses'][str(response.status)] = parsed_response

    def visit_resource(self, resource):
        self.result['components']['schemas'][resource.name] = {
            'type': 'object',
            'required': [field.name for field in resource.fields if field.required],
            'properties': {},
        }

    def visit_list_resource(self, list_resource):
        self.result['components']['schemas'][list_resource.name] = {
            'type': 'array',
            'items': {'$ref': f'#/components/schemas/{list_resource.resource.name}'},
        }

    def _map_field_type(self, element):
        type_ = FIELD_TYPES_MAP.get(element.type, element.extensions.get('openapi.type'))
        if type_ is None:
            raise NotSpecified(f'Type for field {element.type} is not specified for OpenAPI.')
        return type_

    def visit_field(self, field):
        obj = self.result['components']['schemas'][field.parent.name]
        if field.type == fields.ResourceField:
            obj['properties'][field.name] = {'$ref': f'#/components/schemas/{field.resource.name}'}
        else:
            type_ = self._map_field_type(field)

            obj['properties'][field.name] = {'type': type_}

            if getattr(field, 'min_value', None) is not None:
                obj['properties'][field.name]['minimum'] = field.min_value

            if getattr(field, 'max_value', None) is not None:
                obj['properties'][field.name]['maximum'] = field.max_value
