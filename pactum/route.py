class Route:
    def __init__(self, path=None, methods=None):
        if path is None:
            try:
                path = getattr(self, 'path')
            except AttributeError:
                raise TypeError("Missing path specification.")
        self.path = path

        if methods is None:
            methods = getattr(self, 'methods', [])
        self.methods = methods
