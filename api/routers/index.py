from . import orders, order_details, payment_details, customer


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(payment_details.router)
    app.include_router(customer.router)
