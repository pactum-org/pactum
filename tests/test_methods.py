import pytest

from pactum.methods import Method
from pactum.verbs import GET


def test_basic_method():
    test_method = Method(verb=GET, request=None, responses=[])

    assert test_method.verb == GET
    assert test_method.request is None
    assert test_method.responses == []


def test_basic_method_class_def():
    class TestMethod(Method):
        verb = GET
        request = None
        responses = []

    test_method = TestMethod()
    assert test_method.verb == GET
    assert test_method.request is None
    assert test_method.responses == []


def test_method_must_have_responses():
    class TestMethod(Method):
        verb = GET
        request = None

    with pytest.raises(TypeError):
        TestMethod()
