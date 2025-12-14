def count_calls(func):
    call_count = 0
    
    def wrapper(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        result = func(*args, **kwargs)
        return (result, call_count)
    
    return wrapper

@count_calls
def encode(text):
    return text.lower()
