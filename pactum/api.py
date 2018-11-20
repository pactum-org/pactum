from .base import Element


class API(Element):
    _children_name = 'versions'

    def __init__(self, name=None, versions=None):

        if name is None:
            name = getattr(self.__class__, 'name', '')
        self.name = name

        self._initialize_children(locals())
