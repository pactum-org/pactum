class BaseResource:
    def __init__(self, name=None):
        if name is None:
            name = getattr(self, "name", self.__class__.__name__)
        self.name = name


class Resource(BaseResource):
    def __init__(self, name=None, fields=None, behaviors=None):
        super().__init__(name)
        self._mapfields = {}

        if fields is None:
            fields = getattr(self, "fields", [])

        for field in fields:
            if self._mapfields.get(field.name):
                raise AttributeError("Duplicate field names")
            self._mapfields[field.name] = field
        self.fields = fields

        if behaviors is None:
            behaviors = getattr(self, "behavior", [])
        self.behaviors = behaviors

    def __getitem__(self, item):
        return self._mapfields[item]


class ListResource(BaseResource):
    def __init__(self, resource=None, **kwargs):
        super().__init__(**kwargs)

        if resource is None:
            try:
                resource = getattr(self, "resource")
            except AttributeError:
                raise TypeError("Missing resource specification.")

        self.resource = resource
