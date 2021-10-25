from .base import KeyValueElement


class QueryString(KeyValueElement):
    def __init__(self, required=False, empty=True, **kwargs):
        super().__init__(required=required, empty=empty, **kwargs)

    def accept(self, visitor):
        visitor.visit_querystring(self)
