def secret_holder(secret):
    def inner_secret():
        return secret
    return inner_secret
