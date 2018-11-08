from methods import GetMethod
from pactum.routes import Route
from . import resources


product = Route(
    path="/products",
    methods=(
        GetMethod(
            resource=resources.products,
        ),
    )
)
