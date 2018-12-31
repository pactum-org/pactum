class BaseVisitor:
    def visit_api(self, api):
        raise NotImplementedError('visit_api is not implemented')

    def visit_version(self, version):
        raise NotImplementedError('visit_version is not implemented')

    def visit_route(self, route):
        raise NotImplementedError('visit_route is not implemented')

    def visit_action(self, action):
        raise NotImplementedError('visit_action is not implemented')

    def visit_querystring(self, querystring):
        raise NotImplementedError('visit_querystring is not implemented')

    def visit_request(self, request):
        raise NotImplementedError('visit_request is not implemented')

    def visit_response(self, response):
        raise NotImplementedError('visit_response is not implemented')

    def visit_resource(self, resource):
        raise NotImplementedError('visit_resource is not implemented')

    def visit_field(self, field):
        raise NotImplementedError('visit_field is not implemented')

    def visit_list_resource(self, list_resource):
        raise NotImplementedError('visit_list_resource is not implemented')
