def uppercase_elements(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, dict):
            return {k.upper() if isinstance(k, str) else k: v for k, v in res.items()}
        elif isinstance(res, (list, set, tuple)):
            converted = (e.upper() if isinstance(e, str) else e for e in res)
            return type(res)(converted)
        return res
    return wrapper
