class Element:
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
