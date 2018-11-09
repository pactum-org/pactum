from pactum.api import API


def test_base_api():
    api = API(
        name="Test API",
        versions=[],
    )

    assert api.name == "Test API"
    assert len(api.versions) == 0


def test_base_api_class_definition(version):
    class TestAPI(API):
        name = "Test API"
        versions = []

    api = TestAPI()

    assert api.name == "Test API"
    assert len(api.versions) == 0


def test_api_with_one_version(version):
    api = API(
        name="Test API",
        versions=[
            version,
        ],
    )

    assert len(api.versions) == 1


def test_api_class_definition_with_one_version(version):
    class TestAPI(API):
        name = "Test API"
        versions = [
            version,
        ]

    api = TestAPI()
    assert len(api.versions) == 1


def test_api_add_version(api, version):
    api.append(version)
    assert len(api.versions) == 1
