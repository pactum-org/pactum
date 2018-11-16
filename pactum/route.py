class Route:
    def __init__(self, path=None, actions=None):
        if path is None:
            try:
                path = getattr(self, 'path')
            except AttributeError:
                raise TypeError("Missing path specification.")
        self.path = path

        if actions is None:
            actions = getattr(self, 'actions', [])
        self.actions = actions
