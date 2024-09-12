s1 = set([int(s) for s in input().split()])
s2 = set([int(s) for s in input().split()])
d = sorted(s1.difference(s2))
print(*d)
