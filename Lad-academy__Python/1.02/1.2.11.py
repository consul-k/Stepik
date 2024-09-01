a = int(input())
b = int(input())
c = int(input())
if a == b and a != c:
    print(c)
elif b == c and a != c:
    print(a)
else:
    print(b)
