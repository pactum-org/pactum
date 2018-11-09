class API:
    def __init__(self, name=None, versions=None):
        if name is None:
            name = getattr(self, 'name', '')
        self.name = name

        if versions is None:
            versions = getattr(self, 'versions', [])
        self.versions = versions

    def append(self, version):
        self.versions.append(version)
