class Route:
    def __init__(self, path, resource=None, methods=None):
        self.path = path
        self.resource = resource
        self.methods = methods
