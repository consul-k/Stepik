n = int(input())
s1 = set(input())

for i in range(1,n):
    s2 = set(input())
    s1 &= s2

s1 = sorted(s1)
print(*s1)
