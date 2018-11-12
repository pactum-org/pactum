from pactum.route import Route


def test_basic_route(resource):
    route = Route('/test/', resource=resource, methods=[])

    assert route.path == '/test/'
    assert route.resource == resource
    assert len(route.methods) == 0
