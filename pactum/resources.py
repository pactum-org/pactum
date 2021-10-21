from pactum.fields import Field


class BaseResource:
    def __init__(self, name=None):
        if name is None:
            name = getattr(self, 'name', self.__class__.__name__)
        self.name = name


class Resource(BaseResource):
    def __init__(self, name=None, fields=None, behaviors=None):
        super().__init__(name)

        self._mapfields = {}
        self.fields = []
        self._load_fields(fields)

        if behaviors is None:
            behaviors = getattr(self, 'behavior', [])
        self.behaviors = behaviors

    def _load_fields(self, fields):
        if fields is None:
            fields = getattr(self.__class__, 'fields', [])

        for field in fields:
            self._add_field(field.name, field)

        field_class = getattr(self.__class__, 'Fields', None)

        if not field_class:
            return fields

        for name in dir(field_class):
            field = getattr(field_class, name)

            if not isinstance(field, Field):
                continue

            if field.name and field.name != name:
                raise ValueError('Cannot specify a different name to fields')

            self._add_field(name, field)

        return fields

    def _add_field(self, name, field):
        if self._mapfields.get(name):
            raise ValueError('Duplicate field names')

        self.fields.append(field)
        self._mapfields[name] = field
        field.parent = self
        field.name = name

    def __getitem__(self, item):
        return self._mapfields[item]

    def accept(self, visitor):
        visitor.visit_resource(self)
        for field in self.fields:
            field.accept(visitor)


class ListResource(BaseResource):
    def __init__(self, resource=None, **kwargs):
        super().__init__(**kwargs)

        if resource is None:
            try:
                resource = getattr(self, 'resource')
            except AttributeError:
                raise TypeError('Missing resource specification.')

        self.resource = resource

    def accept(self, visitor):
        visitor.visit_list_resource(self)
        self.resource.accept(visitor)
