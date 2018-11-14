from pactum.request import Request


def test_basic_request():
    request = Request(payload=None, headers=[])

    assert request.payload is None
    assert request.headers == []


def test_basic_request_class_def():
    class TestRequest(Request):
        payload = None
        headers = []

    request = TestRequest()

    assert request.payload is None
    assert request.headers == []
