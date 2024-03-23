n = int(input())
m = int(input())
b = n // m
if n % m > 0:
    print(b + 1)
else:
    print(b)
