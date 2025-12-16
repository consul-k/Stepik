def allow_only(*commands):
    def decorator(func):
        def wrapper(cmd, *args, **kwargs):
            if cmd in commands:
                return func(cmd, *args, **kwargs)
            return "Отклонено"
        return wrapper
    return decorator


@allow_only("PING", "SET", "GET")
def dispatch(cmd, value):
    return f"{cmd}:{value}"
