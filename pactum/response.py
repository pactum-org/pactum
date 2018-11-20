class Response:
    def __init__(self, status=None, body=None, headers=None):
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
        if self.body is not None:
            self.body.accept(visitor)
        visitor.visitResponse(self)
