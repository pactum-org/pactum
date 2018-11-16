import pytest

from pactum.methods import Method


def test_basic_method():
    test_method = Method(request=None, responses=[])

    assert test_method.request is None
    assert test_method.responses == []


def test_basic_method_class_def():
    class TestMethod(Method):
        request = None
        responses = []

    test_method = TestMethod()
    assert test_method.request is None
    assert test_method.responses == []


def test_method_must_have_responses():
    class TestMethod(Method):
        request = None

    with pytest.raises(TypeError):
        TestMethod()
