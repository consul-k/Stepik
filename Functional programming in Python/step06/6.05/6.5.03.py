def zip_with_function(args, func):
    return list(map(func, *zip(*zip(*args))))
