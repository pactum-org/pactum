class Field:
    # noinspection PyShadowingBuiltins
    def __init__(self, name=None, type=None):
        if name is None:
            name = getattr(self, "name", "")
        self.name = name

        if type is None:
            type = getattr(self, "type", self.__class__)
        self.type = type


class IntegerField(Field):
    pass


class StringField(Field):
    pass


class ResourceField(Field):
    def __init__(self, name=None, type=None, resource=None):
        super().__init__(name, type)
        if resource is None:
            try:
                resource = getattr(self, "resource")
            except AttributeError:
                raise TypeError("Missing resource specification.")
        self.resource = resource
