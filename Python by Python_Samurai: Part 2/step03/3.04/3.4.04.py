lst = [
    {1, 2}, frozenset({3, 4}), {5, 6}, frozenset({8, 7}),
    {9, 10}, frozenset({11, 12}), {13, 14}, frozenset({16, 15}),
    {17, 18}, frozenset({19, 20}), {21, 22}, frozenset({24, 23})
]        

# продолжите решение здесь
res = frozenset()
for i in lst:
    res = res | i
print(res)
