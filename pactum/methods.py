from base import Element


class GetMethod(Element):
    def __init__(self, *, resource, content_type="", **kwargs):
        super().__init__(**kwargs)
        self.resource = resource
        self.content_type = content_type or "application/json"
