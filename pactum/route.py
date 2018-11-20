class Route:
    def __init__(self, path=None, actions=None):
        if path is None:
            try:
                path = getattr(self, 'path')
            except AttributeError:
                raise TypeError("Missing path specification.")
        self.path = path

        self.actions = []
        if actions is None:
            actions = getattr(self, 'actions', [])

        for action in actions:
            self.append(action)

    def append(self, child):
        self.actions.append(child)
        child.parent = self
