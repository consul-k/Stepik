s1 = set([int(s) for s in input().split()])
s2 = set([int(s) for s in input().split()])
sort = sorted(s1.intersection(s2))
print(*sort)
