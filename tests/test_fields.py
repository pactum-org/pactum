import pytest

from pactum.fields import Field, IntegerField, StringField, ResourceField
from pactum.resources import Resource


def test_basic_field():
    field = Field(
        name="TestField",
        type="type",
    )

    assert field.name == "TestField"
    assert field.type == "type"


def test_basic_field_class_definition():
    class TestField(Field):
        name = "TestField"
        type = "type"

    field = TestField()
    assert field.name == "TestField"
    assert field.type == "type"


def test_basic_field_class_definition_with_class_name():
    class MyField(Field):
        name = "name"

    field = MyField()
    assert field.name == "name"
    assert field.type is MyField


def test_field_type_can_be_class_name():
    field = Field(
        name="TestField",
    )

    assert field.name == "TestField"
    assert field.type == Field


def test_integer_field():
    int_field = IntegerField(name="my_name")

    assert int_field.type == IntegerField
    assert int_field.name == "my_name"


def test_string_field():
    str_field = StringField(name="my_name")

    assert str_field.type == StringField
    assert str_field.name == "my_name"


def test_resource_field(resource):
    resource_field = ResourceField(name="my_field", resource=resource)

    assert resource_field.type == ResourceField
    assert resource_field.name == "my_field"
    assert resource_field.resource == resource


def test_resource_field_class_def(resource):
    class TestResourceField(ResourceField):
        name = "my_field"
        resource = Resource()

    resource_field = TestResourceField()

    assert resource_field.type == TestResourceField
    assert resource_field.name == "my_field"
    assert isinstance(resource_field.resource, Resource)


def test_fails__forresource_field_missing_ressource(resource):
    class TestResourceField(ResourceField):
        name = "my_field"

    with pytest.raises(TypeError):
        TestResourceField()
