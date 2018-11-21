class Response:
    def __init__(self, status=None, body=None, headers=None, description=None):
        if description is None:
            description = getattr(self, 'description', self.__doc__ or '')
        self.description = description.strip()

        if body is None:
            body = getattr(self, 'body', None)
        self.body = body

        if headers is None:
            headers = getattr(self, 'headers', [])
        self.headers = headers

        if status is None:
            try:
                status = getattr(self, 'status')
            except AttributeError:
                raise TypeError('Missing status specification.')
        self.status = status

    def accept(self, visitor):
        visitor.visit_response(self)
        if self.body is not None:
            self.body.accept(visitor)
