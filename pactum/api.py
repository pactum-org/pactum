from .base import Element


class API(Element):
    _children_name = 'versions'

    def __init__(self, name=None, versions=None, description=None):
        if description is None:
            description = getattr(self, 'description', self.__doc__ or '')
        self.description = description.strip()

        if name is None:
            name = getattr(self.__class__, 'name', '')
        self.name = name

        self._initialize_children(locals())

    def accept(self, visitor):
        visitor.visit_api(self)
        for version in self.versions:
            version.accept(visitor)
