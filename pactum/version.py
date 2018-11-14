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

        actions = set()
        for route in routes:
            for method in route.methods:
                action = (route.path, method.verb)
                if action in actions:
                    raise AttributeError('Ambiguous route and method definition.')
                actions.add(action)

        self.routes = routes
