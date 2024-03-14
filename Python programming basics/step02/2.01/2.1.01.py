import math

a = 23
b = 47
c = 12
d = 8
e = 31

x = (a**c)%b
y = round(d/e, 3)
s = round(math.sqrt((x**y)*c),2)

print(f'X = {x}')
print(f'Y = {y}')
print(f'Квадратный корень из S = {s}')
