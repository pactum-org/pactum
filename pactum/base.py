class Element:
    _children_name = None

    def __init__(self, *, parent=None, description=None, extensions=None, **kwargs):
        self.parent = parent

        if description is None:
            description = getattr(self, 'description', self.__doc__ or '')
        self.__doc__ = description.strip()

        if extensions is None:
            extensions = getattr(self, 'extensions', {})
        self.extensions = extensions

    # TODO: refactor this to use kwargs and remove locals() references on caller
    def _initialize_children(self, attrs):
        setattr(self, self._children_name, [])

        children = attrs.get(self._children_name)
        if children is None:
            children = getattr(self.__class__, self._children_name, [])

        for child in children:
            self.append(child)

    def append(self, child):
        child_attr = getattr(self, self._children_name, [])
        child_attr.append(child)
        child.parent = self


# noinspection PyShadowingBuiltins
class KeyValueElement(Element):
    def __init__(self, *, name=None, type=None, required=None, empty=None, **kwargs):
        super().__init__(**kwargs)

        self.name = self._config_default(name=name, default='')
        self.type = self._config_default(type=type, default=self.__class__)
        self.required = self._config_default(required=required, default=True)
        self.empty = self._config_default(empty=empty, default=False)

    def _config_default(self, *, default=None, **kwargs):
        try:
            attr, value = kwargs.popitem()
        except KeyError:
            return default

        if value is not None:
            return value

        attr_value = getattr(self, attr, None)
        if attr_value is not None:
            return attr_value

        return default
