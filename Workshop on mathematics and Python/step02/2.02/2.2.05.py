import math

a = float(input())

hex_area = (3 * math.sqrt(3) * a**2) / 2
tri_area = (math.sqrt(3) * a**2) / 4
total_area = hex_area + 5 * tri_area
print(round(total_area))
