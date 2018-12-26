from unittest.mock import call, MagicMock, Mock
import pytest

from pactum.fields import Field, IntegerField, PositiveIntegerField, ResourceField, StringField, DecimalField
from pactum.resources import Resource


def test_basic_field():
    field = Field(
        name='TestField',
        type='type',
    )

    assert field.name == 'TestField'
    assert field.type == 'type'


def test_basic_field_class_definition():
    class TestField(Field):
        name = 'TestField'
        type = 'type'

    field = TestField()
    assert field.name == 'TestField'
    assert field.type == 'type'


def test_basic_field_class_definition_with_class_name():
    class MyField(Field):
        name = 'name'

    field = MyField()
    assert field.name == 'name'
    assert field.type is MyField


def test_field_type_can_be_class_name():
    field = Field(
        name='TestField',
    )

    assert field.name == 'TestField'
    assert field.type == Field


def test_integer_field():
    int_field = IntegerField(name='my_name')

    assert int_field.type == IntegerField
    assert int_field.name == 'my_name'
    assert int_field.min_value is None
    assert int_field.max_value is None


def test_integer_field_class_field():
    class MyIntegerField(IntegerField):
        min_value = -5
        max_value = 5

    int_field = MyIntegerField()
    assert int_field.min_value == -5
    assert int_field.max_value == 5


def test_integer_field_min_max_values():
    int_field = IntegerField(name='my_name', min_value=-5, max_value=5)

    assert int_field.type == IntegerField
    assert int_field.min_value == -5
    assert int_field.max_value == 5


def test_positive_integer_field():
    int_field = PositiveIntegerField(name='my_name')

    assert int_field.type == PositiveIntegerField
    assert int_field.min_value == 0


def test_string_field():
    str_field = StringField(name='my_name')

    assert str_field.type == StringField
    assert str_field.name == 'my_name'


def test_resource_field(resource):
    resource_field = ResourceField(name='my_field', resource=resource)

    assert resource_field.type == ResourceField
    assert resource_field.name == 'my_field'
    assert resource_field.resource == resource


def test_resource_field_class_def(resource):
    class TestResourceField(ResourceField):
        name = 'my_field'
        resource = Resource()

    resource_field = TestResourceField()

    assert resource_field.type == TestResourceField
    assert resource_field.name == 'my_field'
    assert isinstance(resource_field.resource, Resource)


def test_fails__forresource_field_missing_ressource(resource):
    class TestResourceField(ResourceField):
        name = 'my_field'

    with pytest.raises(TypeError):
        TestResourceField()


def test_basic_decimal_field():
    dec_field = DecimalField(name='dec_field', precision=2)

    assert dec_field.type == DecimalField
    assert dec_field.name == 'dec_field'
    assert dec_field.precision == 2


def test_basic_decimal_field_class_definition():
    class MyDecimalField(DecimalField):
        name = 'dec_field'
        precision = 2

    dec_field = MyDecimalField()

    assert dec_field.type == MyDecimalField
    assert dec_field.name == 'dec_field'
    assert dec_field.precision == 2


def test_fail_basic_decimal_field_no_precision():
    with pytest.raises(TypeError):
        DecimalField(name='dec_field')


def test_initialization_with_parameters_none():
    field = Field(name=None, type=None, description=None)
    assert field.type is Field
    assert field.name == ''
    assert field.__doc__ == ''


def test_accept_method_calls_visit():
    mock_wrapper = Mock()
    mock_wrapper.mocked_visitor = MagicMock()
    field = Field(
        name='TestField',
        type='type',
    )

    field.accept(mock_wrapper.mocked_visitor)

    assert mock_wrapper.mock_calls == [
        call.mocked_visitor.visit_field(field)
    ]
