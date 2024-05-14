a = int(input())
b = int(input())
c = int(input())
p = a+b+c
ph = 1/2 * p
res = (ph * (ph - a) * (ph - b) * (ph - c)) ** 0.5
print(p)
print(res)
