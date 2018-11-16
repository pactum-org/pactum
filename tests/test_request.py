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
