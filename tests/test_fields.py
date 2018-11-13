from pactum.fields import Field


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
