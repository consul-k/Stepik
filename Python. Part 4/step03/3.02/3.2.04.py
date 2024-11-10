def requires_role(required_role):
    def decorator(func):
        def wrapper(role, *args, **kwargs):
            if role == required_role:
                return func(role, *args, **kwargs)
            else:
                print("Доступ запрещен!")
        return wrapper
    return decorator
