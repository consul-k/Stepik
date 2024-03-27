n = int(input())
k = int(input())
s = input().lower()
res = 0
for i in range(n):
    i = input().lower()
    if s.find(i) != -1:
        res += 1
print(res*k)
