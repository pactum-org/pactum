# Pactum
## The HTTP-API specification sketchbook for pythonistas

[![Circle CI](https://circleci.com/gh/pactum-org/pactum.svg?style=svg)](https://circleci.com/gh/pactum-org/pactum)
[![Coverage Status](https://coveralls.io/repos/github/pactum-org/pactum/badge.svg?branch=master)](https://coveralls.io/github/pactum-org/pactum?branch=master)

```shell
pip install pactum
```

With `Pactum` you can **specify** HTTP-APIs using pure python.

Pactum is easy to use, easy to extend and easy to contribute:

### Easy to use

The only requirements to start writing an API specification with `pactum`
is `pactum` package itself and some knowledge of python.

```python
import pactum

class MyAPI(pactum.API):
    name = 'My API'
    versions = [...]
```

### Easy to extend

Using the [visitor pattern](http://wiki.c2.com/?VisitorPattern) you can create
exporters and extensions for any format or service you want.

Take a look at [pactum/exporters/openapi.py](https://github.com/pactum-org/pactum/blob/master/pactum/exporters/openapi.py).

### Architecture

Always keep [this diagram](https://github.com/pactum-org/pactum/wiki/Architecture-Diagram) in mind when defining your APIs.


### Tutorial

Create a file called specs.py and start defining your API.

You can define a `Resource` object for your API.

```python
from pactum import Action, API, Resource, Response, Version
from pactum import fields, verbs

class Order(Resource):
    fields = [
        fields.IntegerField(name='code', required=True),
        fields.TimestampField(name='created_at'),
        fields.StringField(name='item')
    ]
resource = Order()

error_resource = Resource(
    name = 'ErrorResource'
    fields = [fields.StringField(name='error', required=False)]
)
```
You can define any element of your specification by calling it directly as in
`error_resource` or by class definition as in `MyResource` and then calling it.


List resources are definitions of lists of the same resource.
```python
list_order_resource = ListResource(resource=resource)
```

You can define `Response` objects with `status`, `description`(optional)  a
`header`(optional) and a `Resource`/`ListResource` object as `body` (optionally)...

```python
list_response = Response(
    status=200, description='Here is your orders list.', body=list_resource
)

detail_response = Response(
    status=200, description='Here is your order.', body=resource
)

error_response = Response(status=404, resource=error_resource, headers=[('Content-type': 'application-json')])
```

... and `Request` objects with `verb`, `description`, `header`(optional) and a `Resource`/`ListResource`
object as `payload`.

```python
get_request = Request(verb=verbs.GET)
```

An `Action` groups your request and a list of responses for a specified action passed in the description parameter.
```python
list_action = Action(
    description='Returns a list of resources.',
    request=get_request,
    responses=[error_response, list_response]
)

detail_action = Action(
    description='Returns a resource based on its code.',
    request=get_request,
    responses=[error_response, detail_response]
)


```
The Action object, as all other elements in Pactum, receive a description string
that sets the `.__doc__` attribute and can be the docstring of the class
if the object is defined by class definition.

A route can have a list of actions in an HTTP path.
```python
class OrderListRoute(Route):
    path = '/orders'
    actions = [list_action]

list_route = OrderListRoute()

detail_route = OrderRoute(path='/orders/{code}', actions=detail_action)
```

Your routes can be grouped in API versions.
```python
class V1(Version):
    name = 'V1'
    routes = [list_route, detail_route]

v1 = V1()
```
Then you can define your API. ;)
```python
class OrdersAPI(API):
    name = 'Orders API'
    versions = [v1]

api = OrdersAPI()
```
Be happy and ready to export your specification to any format you want.

# Exporting to openapi specs.
Pactum has a command that exports your specification to OpenAPI. You can call it by using:
```
pactum-openapi <spec_file.py> <output_file> [--format=<json or yaml>]
```


# Road to version 1.
- [x] Test elements .accept(visitor) methods.
- [ ] Support for version selectors (Versions should be specified on HTTP header, path, or custom fields)
- [x] Stabilize the way we work with path parameters.
- [ ] Support for Authorization and Authentication Specifications.
- [ ] Support for extensions.
- [ ] Behaviors
