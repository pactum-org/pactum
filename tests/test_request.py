from pactum.request import Request
from pactum.verbs import GET


def test_basic_request():
    request = Request(verb=GET, payload=None, headers=[])

    assert request.verb == GET
    assert request.payload is None
    assert request.headers == []


def test_basic_request_class_def():
    class TestRequest(Request):
        payload = None
        verb = GET
        headers = []

    request = TestRequest()

    assert request.verb == GET
    assert request.payload is None
    assert request.headers == []
