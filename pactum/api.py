class ElementMeta(type):
    def __new__(mcs, name, bases, attrs):
        new_class = super().__new__(mcs, name, bases, attrs)

        children_name = attrs.get('__children_name__', 'children')
        for parent in new_class.mro():
            original_property = getattr(parent, children_name, None)
            if original_property:
                break
        else:
            original_property = None

        for obj_name, obj in attrs.items():
            if obj_name == children_name:
                setattr(mcs, name, original_property)
                setattr(mcs, f"_{name}", obj)
            else:
                setattr(mcs, name, obj)

        return new_class


class Element(metaclass=ElementMeta):
    _children = []

    def append(self, child):
        self._children.append(child)
        child.parent = self


class API(Element):

    __children_name__ = 'versions'

    def __init__(self, name=None, versions=None):
        super().__init__()

        if name is None:
            name = getattr(self, 'name', '')
        self.name = name

        if versions is None:
            versions = getattr(self.__class__, 'versions', [])

        for version in versions:
            self.append(version)

    @property
    def versions(self):
        return self._children
