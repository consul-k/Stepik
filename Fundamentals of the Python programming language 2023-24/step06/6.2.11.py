import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
x3, y3 = map(float, input().split())

a = distance(x1, y1, x2, y2)
b = distance(x2, y2, x3, y3)
c = distance(x3, y3, x1, y1)

perimeter = a + b + c

print(perimeter)
