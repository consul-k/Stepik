def улучшить_щит(func):
    def wrapper():
        return func() * 2
    return wrapper

@улучшить_щит
def щит():
    return 100
