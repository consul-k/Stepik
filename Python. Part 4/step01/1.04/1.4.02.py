def order_pizza(*args):
    if len(args) == 0:
        return "Pizza with: cheese"
    else:
        return f"Pizza with: {', '.join(args)}"
