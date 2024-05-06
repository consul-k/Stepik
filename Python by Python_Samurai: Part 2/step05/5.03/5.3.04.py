lst = [[1, 2, 3, 4], ['s', 'f', 'r'], [1, '3', 5, 'w'],
       [True, False, None], [1, True, 'w', 4.5, {'k': 'v'}]]

# продолжите решение здесь
def func(lst, sep=""):
    result = []
    for inner_list in lst:
        result.append("".join(str(item) for item in inner_list))
    return sep.join(result)
