from .resource import Resource
from .route import Route


class Version:
    def __init__(self, name=None, routes=None, resources=None):
        if routes is not None and resources is not None:
            raise TypeError("Cannot define version with both routes and resources.")
        if routes is None and resources is None:
            raise TypeError("Version must have routes or resources.")
        self.name = name
        self.routes = routes
        self.resources = resources

    def append(self, thing):
        if isinstance(thing, Route) and self.resources is None:
            self.routes.append(thing)
        elif isinstance(thing, Resource) and self.routes is None:
            self.resources.append(thing)
        else:
            raise TypeError(f"Cannot append {thing.__class__.__name__}.")
