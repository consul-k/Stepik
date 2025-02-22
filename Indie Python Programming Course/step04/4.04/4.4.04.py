n = int(input())
s = []
while n > 0:
    s.append(n%10)
    n//=10
print(min(s))
print(max(s))
