n = int(input())

while n >= 10:
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    n = s

print(n)
