import pytest

from pactum.action import Action


def test_basic_action():
    test_action = Action(request=None, responses=[], description="Test action")

    assert test_action.request is None
    assert test_action.responses == []
    assert test_action.description == "Test action"


def test_basic_action_class_def(response):
    class TestAction(Action):
        request = None
        responses = [response]
        description = "Test Action"

    test_action = TestAction()
    assert test_action.request is None
    assert len(test_action.responses) == 1
    assert test_action.responses[0].parent == test_action
    assert test_action.description == "Test Action"


def test_basic_action_class_def_with_doc_description(response):
    class TestAction(Action):
        '''Test Action.'''
        request = None
        responses = [response]

    test_action = TestAction()
    assert test_action.request is None
    assert len(test_action.responses) == 1
    assert test_action.responses[0].parent == test_action
    assert test_action.description == "Test Action."


def test_action_must_have_responses():
    class TestAction(Action):
        request = None

    with pytest.raises(TypeError):
        TestAction()
