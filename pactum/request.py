class Request:
    def __init__(self, verb=None, payload=None, headers=None):
        if verb is None:
            try:
                verb = getattr(self, 'verb')
            except AttributeError:
                raise TypeError('Missing request verb.')
        self.verb = verb

        if payload is None:
            payload = getattr(self, 'payload', None)
        self.payload = payload

        if headers is None:
            headers = getattr(self, 'headers', [])
        self.headers = headers
