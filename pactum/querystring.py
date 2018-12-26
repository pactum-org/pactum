from .base import KeyValueElement


class Querystring(KeyValueElement):
    def accept(self, visitor):
        visitor.visit_querystring(self)
