from . import orders, order_details, payment_details, customer, rating


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(payment_details.router)
    app.include_router(customer.router)
    app.include_router(rating.router)
