from unittest.mock import call, MagicMock, Mock
from pactum.querystring import Querystring


def test_basic_field():
    qs = Querystring(
        name='TestField',
        type='type',
    )

    assert qs.name == 'TestField'
    assert qs.type == 'type'


def test_basic_field_class_definition():
    class TestQuerystring(Querystring):
        name = 'TestQuerystring'
        type = 'type'

    qs = TestQuerystring()
    assert qs.name == 'TestQuerystring'
    assert qs.type == 'type'


def test_basic_field_class_definition_with_class_name():
    class MyQuerystring(Querystring):
        name = 'name'

    qs = MyQuerystring()
    assert qs.name == 'name'
    assert qs.type is MyQuerystring


def test_field_type_can_be_class_name():
    qs = Querystring(
        name='TestField',
    )

    assert qs.name == 'TestField'
    assert qs.type == Querystring


def test_initialization_with_parameters_none():
    qs = Querystring(name=None, type=None, description=None)
    assert qs.name == ''
    assert qs.type == Querystring
    assert qs.__doc__ == ''


def test_accept_method_calls_visit():
    mock_wrapper = Mock()
    mock_wrapper.mocked_visitor = MagicMock()

    querystring = Querystring(
        name='test_querystring',
    )
    querystring.accept(mock_wrapper.mocked_visitor)

    mock_wrapper.mock_calls = [
        call.mocked_visitor.visit_querystring(querystring)]
