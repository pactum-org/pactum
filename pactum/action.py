class Action:
    def __init__(self, request=None, responses=None):
        if request is None:
            request = getattr(self, 'request', None)
        self.request = request

        if responses is None:
            try:
                responses = getattr(self, 'responses')
            except AttributeError:
                raise TypeError('Missing responses specification.')
        self.responses = responses
