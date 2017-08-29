from pactum.version import Version

from . import routes

v1 = Version(
    name="1.0",
    selector_option="/v1",
    routes=(
        routes.product,
    ),
)
