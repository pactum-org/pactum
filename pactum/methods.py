class Method:
    def __init__(self, verb=None, request=None, responses=None):
        if verb is None:
            verb = getattr(self, 'verb', '')
        self.verb = verb

        if request is None:
            request = getattr(self, 'request', None)
        self.request = request

        if responses is None:
            try:
                responses = getattr(self, 'responses')
            except AttributeError:
                raise TypeError('Missing responses.')
        self.responses = responses
