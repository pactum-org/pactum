from pactum.resources import Resource


def test_basic_resource():
    resource = Resource(
        name="TestResource",
        fields=[],
        behaviors=[],
    )

    assert resource.name == "TestResource"
    assert len(resource.fields) == 0
    assert len(resource.behaviors) == 0


def test_basic_resource_class_definition():
    class TestResource(Resource):
        name = "TestResource"
        fields = []
        behaviors = []

    resource = TestResource()
    assert resource.name == "TestResource"
    assert len(resource.fields) == 0
    assert len(resource.behaviors) == 0


def test_basic_resource_class_definition_with_class_name():
    class MyResource(Resource):
        fields = []
        behaviors = []

    resource = MyResource()
    assert resource.name == "MyResource"
    assert len(resource.fields) == 0
    assert len(resource.behaviors) == 0
