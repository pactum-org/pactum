class Behavior:
    pass


class Notification(Behavior):
    def __init__(self, target=None):
        super().__init__()

        if target is None:
            try:
                target = getattr(self, 'target')
            except AttributeError:
                raise TypeError('Missing target specification.')
        self.target = target
