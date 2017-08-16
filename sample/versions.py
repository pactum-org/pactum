from contract.version import Version, VersionSelector

v1 = Version(
    name="1.0",
    selector=VersionSelector.PATH,
    path="v1",
    endpoints=(),
)
