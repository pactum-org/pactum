from pactum.querystring import Querystring


def test_basic_field():
    qs = Querystring(
        name="TestField",
        type="type",
    )

    assert qs.name == "TestField"
    assert qs.type == "type"


def test_basic_field_class_definition():
    class TestQuerystring(Querystring):
        name = "TestQuerystring"
        type = "type"

    qs = TestQuerystring()
    assert qs.name == "TestQuerystring"
    assert qs.type == "type"


def test_basic_field_class_definition_with_class_name():
    class MyQuerystring(Querystring):
        name = "name"

    qs = MyQuerystring()
    assert qs.name == "name"
    assert qs.type is MyQuerystring


def test_field_type_can_be_class_name():
    qs = Querystring(
        name="TestField",
    )

    assert qs.name == "TestField"
    assert qs.type == Querystring
