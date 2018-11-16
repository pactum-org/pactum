from pactum import fields, verbs
from pactum.api import API
from pactum.methods import Method
from pactum.request import Request
from pactum.resources import ListResource, Resource
from pactum.response import Response
from pactum.route import Route
from pactum.version import Version


class SKUField(fields.Field):
    pass


class MoneyField(fields.DecimalField):
    precision = 2


class ItemResource(Resource):
    fields = [
        fields.IntegerField(name="id"),
        fields.PositiveIntegerField(name="quantity"),
        SKUField(name="sku"),
        fields.StringField(name="description"),
        MoneyField(name="price", precision=2),
        MoneyField(name="total", precision=2),
    ]


class ItemListResource(ListResource):
    resource = ItemResource()


class OrderResource(Resource):
    fields = [
        fields.StringField(name="code"),
        fields.TimestampField(name="created_at"),
        fields.ResourceField(name="items", resource=ItemListResource),
        MoneyField(name="total"),
    ]


class OrderListResource(ListResource):
    resource = OrderResource()


class OrderListRoute(Route):
    path = "/orders"
    methods = [
        Method(
            request=Request(verb=verbs.GET),
            responses=[
                Response(
                    status=200,
                    body=OrderListResource())
            ],
        )
    ]


api = API(
    name="Orders API",
    versions=[
        Version(
            name="v1",
            routes=[
                OrderListRoute(),
            ]
        )
    ]
)
