def cache_one_arg(func):
    cache = {}

    def wrapper(x):
        if x in cache:
            print(f"HIT {x}")
            return cache[x]
        else:
            print(f"MISS {x}")
            result = func(x)
            cache[x] = result
            return result
    
    return wrapper


@cache_one_arg
def telemetry(x):
    return x * x + 1
