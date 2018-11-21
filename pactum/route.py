from .base import Element


class Route(Element):
    _children_name = 'actions'

    def __init__(self, path=None, actions=None):
        if path is None:
            try:
                path = getattr(self, 'path')
            except AttributeError:
                raise TypeError("Missing path specification.")
        self.path = path

        self._initialize_children(locals())

    def accept(self, visitor):
        visitor.visit_route(self)
        for action in self.actions:
            action.accept(visitor)
