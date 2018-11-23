# pactum
## The HTTP-API specification sketchbook for pythonistas

.. image:: https://circleci.com/gh/olist/pactum.svg?style=svg
    :target: https://circleci.com/gh/olist/pactum
.. image:: https://coveralls.io/repos/github/osantana/pactum/badge.svg?branch=master
    :target: https://coveralls.io/github/osantana/pactum?branch=master


With pactum you will be able to:

- Define HTTP-API specifications using pure python. (Easy to use)
  The only requirement to start writing an API specification with pactum is
  pactum itself and some knowledge of python.


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

- Tooling created using idiomatic code. (Easy to contribute)

```python

```

- Plugable architecture for exporters (Easy-to-extend)
```python
from pactum.visitors import BaseVisitor
class MyExporter(BaseVisitor):
    def visit_api(self, api):
        print(f'{api.name}')

    def visit_version(self, version):
       print(f'{version.name} for {version.parent.name}')
```

# What is pactum and why?

Pactum is a tool to define HTTP API specifications that uses
idiomatic python to define your APIs. With pactum you can define your
HTTP API with pure python and export it to whatever format you want.

# Architecture

We discovered a python-idiomatic architecture to define HTTP-APIs.


# Tutorial

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
