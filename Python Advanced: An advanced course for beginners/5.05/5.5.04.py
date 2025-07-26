a = int(input())
b = int(input())
c = int(input())

x_v = -b / (2 * a)
y_v = a * x_v**2 + b * x_v + c

print((x_v, y_v))
