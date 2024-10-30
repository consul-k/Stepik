def s(lst):
    res = []
    for i in numbers:
        if i**2 < 50:
            res.append(i**2)
    return res

print(s(numbers))
