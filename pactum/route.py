import re
from .base import Element


class Route(Element):
    _children_name = 'actions'

    def __init__(self, path=None, actions=None, **kwargs):
        super().__init__(**kwargs)
        if path is None:
            try:
                path = getattr(self, 'path')
            except AttributeError:
                raise TypeError("Missing path specification.")
        self.path = path
        self.parameters = self._get_parameters(path)

        self._initialize_children(locals())

    def _get_parameters(self, path):
        parameters_re = re.compile(r'\{(?P<parameter>[\.\w-]+)\}')
        return parameters_re.findall(path)

    def accept(self, visitor):
        visitor.visit_route(self)
        for action in self.actions:
            action.accept(visitor)
