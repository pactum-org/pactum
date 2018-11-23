# Pactum
## The HTTP-API specification sketchbook for pythonistas

[![Circle CI](https://circleci.com/gh/olist/pactum.svg?style=svg)](https://circleci.com/gh/olist/pactum)

```shell
pip install pactum
```

With `Pactum` you can **specify** HTTP-API using pure python.


Pactum is easy to use, easy to extend and easy to contribute:

- Easy to use

The only requirement to start writing an API specification with `pactum`
is `pactum` itself and some knowledge of python.

```python
import pactum

class MyAPI(API):
    name = 'My API'
    versions = [...]
```

- Easy to extend

Using the [visitor pattern](http://wiki.c2.com/?VisitorPattern) you can create
exporters and extensions for any format or service you want.

Take a look at [pactum/exporters/openapi.py](pactum/exporters/openapi.py).

- Easy to contribute

Tooling created using idiomatic code. (Easy to contribute)

```python

```


# Architecture

We discovered a python-idiomatic architecture to define HTTP-APIs.


# Tutorial
```python
from pactum import Action, API, Resource, Response, Version
from pactum import fields, verbs

class MyResource(Resource):
    fields = [
        fields.IntegerFieldField(name='code', required=True),
        fields.StringField(name='item')
    ]
resource = MyResource()

class ErrorResource(Resource):
    fields = [
        fields.StringField(name='error', requried=False)
    ]
error_resource = ErrorResource()

list_resource = MyListResource(resource=resource)

ok_response = Response(
    status=200, description='Here is your resource list.', body=list_resource
)

error_response = Response(status=400, resource=error_resource)
request = Request(verb=verbs.GET, name='my_request')

action = Action(
    description='Returns a list of resources.',
    request=request, responses=[error_response, ok_response]
)

class Route(Route):
    path = '/resource'
    action = [action]

class V1(Version):
    name = 'V1'

v1 = V1()

class MyAPI(API):
    name = 'My API'
    versions = [v1]

api = MyAPI()
```

# Exporters
Visitor design pattern. (http://wiki.c2.com/?VisitorPattern)


# Road to version 1.
- [ ] Test elements .accept(visitor) methods.
- [ ] Support for version selectors (Versions should be specified on HTTP header, path, or custom fields)
- [ ] Stabilize the way we work with path parameters.
- [ ] Support for Authorization and Authentication Specifications.
- [ ] Support for extensions.
- [ ] Behaviors



Create API specifications and documentation using Python.
