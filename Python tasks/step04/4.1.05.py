lst = []
i = int(input())
while i != 0:
    lst.append(i)
    i = int(input())
print(sorted(set(lst)))
