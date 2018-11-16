import pytest

from pactum.action import Action


def test_basic_action():
    test_action = Action(request=None, responses=[])

    assert test_action.request is None
    assert test_action.responses == []


def test_basic_action_class_def():
    class TestAction(Action):
        request = None
        responses = []

    test_action = TestAction()
    assert test_action.request is None
    assert test_action.responses == []


def test_action_must_have_responses():
    class TestAction(Action):
        request = None

    with pytest.raises(TypeError):
        TestAction()