import math

def geron(a, b, c):
    p = (a + b + c) / 2  # полупериметр
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area
