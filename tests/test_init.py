def test_API_can_be_imported_from_module_root():
    from pactum import API
    from pactum.api import API as api_API

    assert API == api_API


def test_Version_can_be_imported_from_pactum():
    from pactum import Version
    from pactum.version import Version as api_Version

    assert Version == api_Version
