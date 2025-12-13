def log_command(func):
    def wrapper(*args, **kwargs):
        print(f"START {func.__name__}")
        result = func(*args, **kwargs)
        print(f"RESULT {result}")
        print(f"END {func.__name__}")
        return result
    return wrapper

@log_command
def send_command(a, b):
    return a + b
