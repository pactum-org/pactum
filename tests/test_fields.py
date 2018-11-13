from pactum.fields import Field, IntegerField, StringField, ResourceField


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


def test_integer_field():
    int_field = IntegerField(name="my_name")

    assert int_field.type == IntegerField
    assert int_field.name == "my_name"


def test_string_field():
    str_field = StringField(name="my_name")

    assert str_field.type == StringField
    assert str_field.name == "my_name"


def test_embeded_field(resource):
    embeded_field = ResourceField(name="my_field", resource=resource)

    assert embeded_field.type == ResourceField
    assert embeded_field.name == "my_field"
    assert embeded_field.resource == resource
