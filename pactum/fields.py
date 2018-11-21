class Field:
    # noinspection PyShadowingBuiltins
    def __init__(self, name=None, type=None):
        if name is None:
            name = getattr(self, "name", "")
        self.name = name

        if type is None:
            type = getattr(self, "type", self.__class__)
        self.type = type

    def accept(self, visitor):
        visitor.visit_field(self)


class IntegerField(Field):
    def __init__(self, min_value=None, max_value=None, **kwargs):
        super().__init__(**kwargs)

        if min_value is None:
            min_value = getattr(self, "min_value", None)
        self.min_value = min_value

        if max_value is None:
            max_value = getattr(self, "max_value", None)
        self.max_value = max_value


class PositiveIntegerField(IntegerField):
    min_value = 0


class DecimalField(Field):
    def __init__(self, precision=None, **kwargs):
        super().__init__(**kwargs)

        if precision is None:
            try:
                precision = getattr(self, "precision")
            except AttributeError:
                raise TypeError("Missing precision specification.")

        self.precision = precision


class StringField(Field):
    pass


class TimestampField(Field):
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
