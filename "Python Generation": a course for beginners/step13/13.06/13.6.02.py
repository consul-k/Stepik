import math

def get_circle(radius):
    c = 2 * math.pi * radius
    s = math.pi * radius**2
    return c, s

radius = float(input())
print(*get_circle(radius))
