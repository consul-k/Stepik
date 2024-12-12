import math

x_point = float(input())
y_point = float(input())
r_circle = float(input())

hypotenuse = math.sqrt(x_point ** 2 + y_point ** 2)

if hypotenuse <= r_circle:
    print("YES")
else:
    print("NO")
