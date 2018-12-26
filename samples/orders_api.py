import pactum
from pactum import fields, verbs


class SKUField(fields.Field):
    extensions = {'openapi.type': 'string'}


class MoneyField(fields.DecimalField):
    extensions = {'openapi.type': 'float'}
    precision = 2


class ItemResource(pactum.Resource):
    fields = [
        fields.IntegerField(name="id"),
        fields.PositiveIntegerField(name="quantity"),
        SKUField(name="sku"),
        fields.StringField(name="description"),
        MoneyField(name="price", precision=2),
        MoneyField(name="total", precision=2),
    ]


class ItemListResource(pactum.ListResource):
    resource = ItemResource()


class OrderResource(pactum.Resource):
    fields = [
        fields.StringField(name="code"),
        fields.TimestampField(name="created_at"),
        fields.ResourceField(name="items", resource=ItemListResource()),
        MoneyField(name="total"),
    ]


order_resource = OrderResource()


class OrderListResource(pactum.ListResource):
    resource = order_resource


class OrderListRoute(pactum.Route):
    path = "/orders"
    actions = [
        pactum.Action(
            request=pactum.Request(verb=verbs.GET),
            responses=[
                pactum.Response(
                    status=200,
                    body=OrderListResource()
                )
            ],
            description='List Orders'
        )
    ]
    querystrings = [
        pactum.Querystring(
            name='limit', type=fields.IntegerField,
            description='Limits the number of order in the response'
        ),
    ]


class OrderDetailRoute(pactum.Route):
    path = "/order/{code}"
    actions = [
        pactum.Action(
            request=pactum.Request(verb=verbs.GET),
            responses=[
                pactum.Response(
                    status=200,
                    body=order_resource)
            ],
            description='Retrieve order by code.'
        )
    ]


api = pactum.API(
    name="Orders API",
    versions=[
        pactum.Version(
            name="v1",
            routes=[
                OrderListRoute(),
                OrderDetailRoute(),
            ]
        )
    ]
)
