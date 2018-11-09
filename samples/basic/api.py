from pactum.api import API
from samples.basic.versions import FirstVersion


api = API(
    name = "Sample API",
    versions = [
        FirstVersion(),
    ],
)
