def sieve(lst):
    unique = []
    [unique.append(item) for item in reversed(lst) if item not in unique]
    return tuple(unique)

lst = list(map(int, input().split(',')))
print(sieve(lst))
