class Request:
    def __init__(self, payload=None, headers=None):
        if payload is None:
            payload = getattr(self, 'payload', None)
        self.payload = payload

        if headers is None:
            headers = getattr(self, 'headers', [])
        self.headers = headers
