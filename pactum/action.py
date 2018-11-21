from .base import Element


class Action(Element):
    _children_name = 'responses'

    def __init__(self, request=None, responses=None, description=None):
        if description is None:
            description = getattr(self, 'description', self.__doc__ or '')
        self.description = description.strip()

        if request is None:
            request = getattr(self.__class__, 'request', None)
        self.request = request
        if self.request:
            self.request.parent = self

        self.responses = []
        if responses is None:
            try:
                responses = getattr(self.__class__, 'responses')
            except AttributeError:
                raise TypeError('Missing responses specification.')

        self._initialize_children(locals())

    def accept(self, visitor):
        visitor.visitAction(self)
        self.request.accept(visitor)
        for response in self.responses:
            response.accept(visitor)
