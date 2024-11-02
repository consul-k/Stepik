def describe_product(**kwargs):
    components = [f"{key}: {value}" for key, value in kwargs.items()]
    if len(components) == 0:
        return "No product details provided"
    else:
        return "Product details: " + ", ".join(components)
