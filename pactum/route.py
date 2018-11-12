from pactum.base import Element


class Route(Element):
    _http_methods = [
        "get", "post", "put", "patch", "delete",
        "connect", "options", "head", "trace"
    ]

    def __init__(self, *, path, methods, **kwargs):
        super().__init__(**kwargs)
        self.path = path
        self.methods = methods

    @property
    def http_methods(self):
        return self._http_methods
