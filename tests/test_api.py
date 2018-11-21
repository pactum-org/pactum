from pactum.api import API


def test_base_api():
    api = API(
        name="Test API",
        versions=[],
        description='API for tests.'
    )

    assert api.name == "Test API"
    assert api.description == "API for tests."
    assert len(api.versions) == 0


def test_base_api_class_definition(version):
    class TestAPI(API):
        name = "Test API"
        versions = [version]
        description = "API for tests."

    api = TestAPI()

    assert api.name == "Test API"
    assert api.description == "API for tests."
    assert len(api.versions) == 1
    assert api.versions[0].parent == api


def test_api_class_definition_with_doc_description(version):
    class TestAPI(API):
        """
        API for tests.
        """
        name = "Test API"
        versions = [version]

    api = TestAPI()

    assert api.name == "Test API"
    assert api.description == "API for tests."
    assert len(api.versions) == 1
    assert api.versions[0].parent == api


def test_api_with_one_version(version):
    api = API(
        name="Test API",
        versions=[
            version,
        ],
    )

    assert len(api.versions) == 1
    assert api.versions[0].parent == api


def test_api_class_definition_with_one_version(version):
    class TestAPI(API):
        name = "Test API"
        versions = [
            version,
        ]

    api = TestAPI()
    assert len(api.versions) == 1
    assert api.versions[0].parent == api


def test_api_add_version(api, version):
    api.append(version)
    assert len(api.versions) == 1
    assert api.versions[0].parent == api


def test_prefer_parameter_to_class_definition(version):
    class TestAPI(API):
        name = "Test API"
        versions = [version, version]

    api = TestAPI(name="Test API by parameter", versions=[version])

    assert len(api.versions) == 1
    assert api.name == "Test API by parameter"
    assert api.versions[0].parent == api
