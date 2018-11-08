from pactum.api import API
from samples.basic.versions import FirstVersion


class SampleAPI(API):
    name = "Sample API"
    versions = [
        FirstVersion(),
    ]

api = SampleAPI()
