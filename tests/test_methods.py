from pactum.methods import Method
from pactum.verbs import GET


def test_basic_method():
    test_method = Method(verb=GET, action='list')

    assert test_method.verb == GET
    assert test_method.action == 'list'


def test_basic_method_class_def():
    class TestMethod(Method):
        verb = GET
        action = 'list'

    test_method = TestMethod()
    assert test_method.verb == GET
    assert test_method.action == 'list'
