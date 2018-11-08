from pactum.version import Version, version_selector


class FirstVersion(Version):
    class Meta:
        name = "1.0"
        selector = version_selector("/v1")
