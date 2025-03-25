def my_func(collection, n):
    collection = collection.copy()
    for i in range(1, n + 1):
        collection.append(i)
    return collection
