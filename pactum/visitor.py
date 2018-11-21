class BaseVisitor:
    def visit_api(self, api):
        print(f'Visiting API: {api.name}')

    def visit_version(self, version):
        print(f'Visiting Version {version.name} for {version.parent.name}')

    def visit_route(self, route):
        print(f'Visiting Route {route.path}')

    def visit_request(self, request):
        print(f'Visiting Request {request.verb}')

    def visit_response(self, response):
        print(f'Visiting Response {response.status}, {[x for x in response.headers]}')

    def visit_action(self, action):
        print(f'Visition action')

    def visit_resource(self, resource):
        print(f'Visiting Resource {resource.name}.')

    def visit_field(self, field):
        print(f'Visiting Field {field.name}, {field.type}')
