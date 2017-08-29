from contract.base import Element


class Route(Element):
    def __init__(self, path, **kwargs):
        super().__init__(**kwargs)
        self.path = path
