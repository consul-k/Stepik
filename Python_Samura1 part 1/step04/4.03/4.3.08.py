s = list(map(int, (input().split())))
mx = s.index(max(s))
mn = s.index(min(s))
s[mx], s[mn] = s[mn], s[mx]
print(*s)
