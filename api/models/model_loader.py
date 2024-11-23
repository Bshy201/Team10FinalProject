from . import orders, order_details, recipes, sandwiches, resources, payment_details, customer, rating

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    payment_details.Base.metadata.create_all(engine)
    customer.Base.metadata.create_all(engine)
    rating.Base.metadata.create_all(engine)
