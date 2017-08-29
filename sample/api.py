from pactum.api import API
from pactum.version import VersionSelector

from . import versions

api = API(
    name="Sample API",
    version_selector=VersionSelector.PATH,
    versions=(
        versions.v1,
    ),
)
