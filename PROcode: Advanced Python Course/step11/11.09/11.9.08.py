def Outer(func):
    def wrapper(*args, **kwargs):
        print("OUT before")
        result = func(*args, **kwargs)
        print("OUT after")
        return result
    return wrapper

def Inner(func):
    def wrapper(*args, **kwargs):
        print("IN before")
        result = func(*args, **kwargs)
        print("IN after")
        return result
    return wrapper

@Outer
@Inner
def core(a, b):
    return a * b
