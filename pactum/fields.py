class Field:
    # noinspection PyShadowingBuiltins
    def __init__(self, name=None, type=None):
        if name is None:
            name = getattr(self, "name", "")
        self.name = name

        if type is None:
            type = getattr(self, "type", self.__class__)
        self.type = type
