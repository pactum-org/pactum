from unittest.mock import call, MagicMock, Mock
import pytest

from pactum import verbs
from pactum.request import Request


def test_basic_request():
    request = Request(verb=verbs.GET, payload=None, headers=[])

    assert request.verb == verbs.GET
    assert request.payload is None
    assert request.headers == []


def test_basic_request_class_def():
    class TestRequest(Request):
        payload = None
        verb = verbs.GET
        headers = []

    request = TestRequest()

    assert request.verb == verbs.GET
    assert request.payload is None
    assert request.headers == []


def test_fails_if_no_verb():
    with pytest.raises(TypeError):
        Request(payload=None, headers=[])


def test_accept_method_calls_visit_and_payload_accept():
    mock_wrapper = Mock()
    mock_wrapper.mocked_visitor = MagicMock()
    mock_wrapper.mocked_payload = MagicMock()

    request = Request(
        verb='GET',
        payload=mock_wrapper.mocked_payload,
    )
    request.accept(mock_wrapper.mocked_visitor)

    assert mock_wrapper.mock_calls == [
        call.mocked_visitor.visit_request(request),
        call.mocked_payload.accept(mock_wrapper.mocked_visitor)
    ]
