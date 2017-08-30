from pactum.api import API

from . import versions

api = API(
    name="Sample API",
    versions=(
        versions.v1,
    ),
)
