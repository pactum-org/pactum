class BaseVisitor:
    def visitAPI(self, api):
        print(f'Visiting API: {api.name}')

    def visitVersion(self, version):
        print(f'Visiting Version {version.name}')

    def visitRoute(self, route):
        print(f'Visiting Route {route.path}')

    def visitRequest(self, request):
        print(f'Visiting Request {request.verb}')

    def visitResponse(self, response):
        print(f'Visiting Response {response.status}, {[x for x in response.headers]}')

    def visitAction(self, action):
        print(f'Visition action')

    def visitResource(self, resource):
        print(f'Visiting Resource {resource.name}.')

    def visitField(self, field):
        print(f'Visiting Field {field.name}, {field.type}')
