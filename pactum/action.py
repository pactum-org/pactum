from .base import Element


class Action(Element):
    _children_name = 'responses'

    def __init__(self, request=None, responses=None, **kwargs):
        super().__init__(**kwargs)

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
        visitor.visit_action(self)
        if self.request:
            self.request.accept(visitor)
        for response in self.responses:
            response.accept(visitor)
