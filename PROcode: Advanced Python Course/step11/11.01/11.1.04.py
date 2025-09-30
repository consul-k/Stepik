def order_summary(*orders, main_order):
    return {
        "orders": list(orders),
        "main_order": main_order
    }
