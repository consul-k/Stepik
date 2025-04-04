def check_exist_attrs(obj, attrs):
    return {attr: hasattr(obj, attr) for attr in attrs}
