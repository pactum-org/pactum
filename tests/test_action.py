from unittest.mock import call, MagicMock, Mock
import pytest

from pactum.action import Action


def test_basic_action(request, response):
    test_action = Action(request=request, responses=[response], description="Test action")

    assert test_action.request == request
    assert test_action.responses == [response]
    assert test_action.responses[0].parent == test_action
    assert test_action.request.parent == test_action
    assert test_action.__doc__ == "Test action"


def test_basic_action_class_def(response):
    class TestAction(Action):
        request = None
        responses = [response]
        description = "Test Action"

    test_action = TestAction()
    assert test_action.request is None
    assert len(test_action.responses) == 1
    assert test_action.responses[0].parent == test_action
    assert test_action.__doc__ == "Test Action"


def test_basic_action_class_def_with_doc_description(response):
    class TestAction(Action):
        '''Test Action.'''
        request = None
        responses = [response]

    test_action = TestAction()
    assert test_action.request is None
    assert len(test_action.responses) == 1
    assert test_action.responses[0].parent == test_action
    assert test_action.__doc__ == "Test Action."


def test_action_must_have_responses():
    class TestAction(Action):
        request = None

    with pytest.raises(TypeError):
        TestAction()


def test_accept_method_calls_visit_and_response_and_requests_accept():
    mock_wrapper = Mock()
    mock_wrapper.mocked_visitor = MagicMock()
    mock_wrapper.mocked_request = MagicMock()
    mock_wrapper.mocked_response1 = MagicMock()
    mock_wrapper.mocked_response2 = MagicMock()

    action = Action(
        name='Test Action',
        request=mock_wrapper.mocked_request,
        responses=[mock_wrapper.mocked_response1, mock_wrapper.mocked_response2]
    )
    action.accept(mock_wrapper.mocked_visitor)

    assert mock_wrapper.mock_calls[-4:] == [
        call.mocked_visitor.visit_action(action),
        call.mocked_request.accept(mock_wrapper.mocked_visitor),
        call.mocked_response1.accept(mock_wrapper.mocked_visitor),
        call.mocked_response2.accept(mock_wrapper.mocked_visitor),
    ]
