class Element:
    def __init__(self, description=None, extensions=None, **kwargs):
        if description is None:
            description = getattr(self, 'description', self.__doc__ or '')
        self.__doc__ = description.strip()

        if extensions is None:
            extensions = getattr(self, 'extensions', {})
        self.extensions = extensions

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
