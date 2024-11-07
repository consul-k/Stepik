def sequence_generator(start):
    count = start
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
