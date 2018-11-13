class Method:
    def __init__(self, verb=None, action=None):
        if verb is None:
            verb = getattr(self, 'verb', '')
        self.verb = verb

        if action is None:
            action = getattr(self, 'action', '')
        self.action = action
