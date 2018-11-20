from .base import Element


class Version(Element):
    _children_name = 'routes'

    def __init__(self, name=None, routes=None):
        if name is None:
            name = getattr(self, 'name', '')
        self.name = name

        if routes is None:
            try:
                routes = getattr(self.__class__, 'routes')
            except AttributeError:
                raise TypeError("Version must have routes.")

        actions = set()
        for route in routes:
            for action in route.actions:
                action = (route.path, action.request.verb)
                if action in actions:
                    raise AttributeError('Ambiguous route and action request specification.')
                actions.add(action)

        self._initialize_children(locals())
