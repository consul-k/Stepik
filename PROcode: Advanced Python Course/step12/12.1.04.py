def найти_нод(a, b):
    if b == 0:
        return a
    return найти_нод(b, a % b)
