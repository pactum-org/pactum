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


# TODO: Behaviors
# Notification Behavior
# Proxy Behavior
# Persist Behavior
# Transactional Behavior
# Change Behavior
# Scope of behavior? Resource? Field? Both?
