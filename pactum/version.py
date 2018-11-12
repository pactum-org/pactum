from .resource import Resource
from .route import Route


class Version:
    def __init__(self, name=None, routes=None, resources=None):
        if name is None:
            name = getattr(self, 'name', '')
        self.name = name
        if routes is None:
            routes = getattr(self, 'routes', None)
        self.routes = routes
        if resources is None:
            resources = getattr(self, 'resources', None)

        self.resources = resources

        if self.routes is not None and self.resources is not None:
            raise TypeError("Cannot define version with both routes and resources.")
        if self.routes is None and self.resources is None:
            raise TypeError("Version must have routes or resources.")

    def append(self, thing):
        if isinstance(thing, Route) and self.resources is None:
            self.routes.append(thing)
        elif isinstance(thing, Resource) and self.routes is None:
            self.resources.append(thing)
        else:
            raise TypeError(f"Cannot append {thing.__class__.__name__}.")
