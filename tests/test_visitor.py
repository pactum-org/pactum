from pactum.visitor import BaseVisitor


class TestVisitor(BaseVisitor):
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
        return querystring

    def visit_request(self, request):
        self.blueprints.append('request visisted')

    def visit_response(self, response):
        self.blueprints.append('response visited')

    def visit_resource(self, resource):
        self.blueprints.append('resource visited')

    def visit_field(self, field):
        self.blueprints.append('field visited')

    def visit_list_resource(self, list_resource):
        self.blueprints.append('list_resource visited')


def test_visitor_call_order(api):
    visitor = TestVisitor()
    api.accept(visitor)

    assert visitor.blueprints == [
        'api visited',
        'version visited',
        'route visited',
        'action visited',
        'request visisted',
        'resource visited',
        'field visited',
        'response visited',
        'list_resource visited',
        'resource visited',
        'field visited',
        'querystring visited'
    ]
