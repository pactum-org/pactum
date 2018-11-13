from .resources import Resource
from .route import Route


class Version:
    def __init__(self, name=None, routes=None):
        if name is None:
            name = getattr(self, 'name', '')
        self.name = name
        if routes is None:
            try:
                routes = getattr(self, 'routes')
            except AttributeError:
                raise TypeError("Version must have routes.")
        self.routes = routes

    def append(self, route):
        self.routes.append(route)