class API:

    __children_name__ = 'versions'

    def __init__(self, name=None, versions=None):
        super().__init__()

        if name is None:
            name = getattr(self.__class__, 'name', '')
        self.name = name

        self.versions = []
        if versions is None:
            versions = getattr(self.__class__, 'versions', [])

        for version in versions:
            self.append(version)

    def append(self, child):
        self.versions.append(child)
        child.parent = self
