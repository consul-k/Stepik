def add_attrs(**attrs):
    def decorator(func):
        for key, value in attrs.items():
            setattr(func, key, value)
        return func
    return decorator
