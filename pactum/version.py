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
        single_actions = []
        for route in routes:
            for method in route.methods:
                single_actions.append((route.path, method.verb))

        if len(set(single_actions)) < len(single_actions):
            raise AttributeError('Ambiguous methods.')

        self.routes = routes

    def append(self, route):
        self.routes.append(route)
