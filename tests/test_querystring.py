from pactum.querystring import QueryString


def test_basic_field():
    qs = QueryString(
        name='TestField',
        type='type',
    )

    assert qs.name == 'TestField'
    assert qs.type == 'type'


def test_basic_field_defaults():
    qs = QueryString()

    assert qs.name == ''
    assert qs.type == QueryString
    assert not qs.required
    assert qs.empty


def test_basic_field_class_definition():
    class TestQueryString(QueryString):
        name = 'TestQueryString'
        type = 'type'

    qs = TestQueryString()
    assert qs.name == 'TestQueryString'
    assert qs.type == 'type'
    assert not qs.required
    assert qs.empty


def test_basic_field_class_definition_defaults():
    class TestQueryString(QueryString):
        pass

    qs = TestQueryString()
    assert qs.name == ''
    assert qs.type == TestQueryString
    assert not qs.required
    assert qs.empty


def test_basic_field_class_definition_with_class_name():
    class MyQueryString(QueryString):
        name = 'name'

    qs = MyQueryString()
    assert qs.name == 'name'
    assert qs.type is MyQueryString


def test_field_type_can_be_class_name():
    qs = QueryString(
        name='TestField',
    )

    assert qs.name == 'TestField'
    assert qs.type == QueryString


def test_initialization_with_parameters_none():
    qs = QueryString(name=None, type=None, description=None)
    assert qs.name == ''
    assert qs.type == QueryString
    assert qs.__doc__ == ''
