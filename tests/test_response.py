from unittest.mock import call, MagicMock, Mock

import pytest

from pactum.response import Response


def test_basic_response():
    response = Response(status=200, body=None, headers=[])

    assert response.body is None
    assert response.headers == []
    assert response.status == 200


def test_basic_response_class_def():
    class TestResponse(Response):
        body = None
        headers = []
        status = 200

    response = TestResponse()

    assert response.body is None
    assert response.headers == []
    assert response.status == 200


def test_response_is_invalid_without_status():
    class TestResponse(Response):
        body = None
        headers = []

    with pytest.raises(TypeError):
        TestResponse()


def test_response_class_definition_with_doc_description(version):
    class TestResponse(Response):
        """Response for tests."""
        body = None
        headers = []
        status = 200

    response = TestResponse()

    assert response.body is None
    assert response.headers == []
    assert response.status == 200
    assert response.__doc__ == "Response for tests."


def test_accept_method_calls_visit_and_body_accept():
    mock_wrapper = Mock()
    mock_wrapper.mocked_visitor = MagicMock()
    mock_wrapper.mocked_body = MagicMock()

    response = Response(
        status=200,
        body=mock_wrapper.mocked_body,
    )
    response.accept(mock_wrapper.mocked_visitor)

    assert mock_wrapper.mock_calls == [
        call.mocked_visitor.visit_response(response),
        call.mocked_body.accept(mock_wrapper.mocked_visitor)
    ]
