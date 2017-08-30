from pactum.version import Version, version_selector

from . import routes

v1 = Version(
    name="1.0",
    selector=version_selector("/v1"),
    routes=(
        routes.product,
    ),
)
