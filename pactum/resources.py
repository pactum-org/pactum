class Resource:
    def __init__(self, name=None, fields=None, behaviors=None):
        if name is None:
            name = getattr(self, "name", self.__class__.__name__)
        self.name = name

        if fields is None:
            fields = getattr(self, "fields", [])
        self.fields = fields

        if behaviors is None:
            behaviors = getattr(self, "behavior", [])
        self.behaviors = behaviors
