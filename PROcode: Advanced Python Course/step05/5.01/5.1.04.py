import math

n = int(input())

max_distance = -1
farthest_object = (0.0, 0.0)

for _ in range(n):
    x = float(input())
    y = float(input())
    obj = (x, y)

    distance = math.sqrt(x**2 + y**2)

    # Оставляем первый объект при равенстве расстояний
    if distance > max_distance:
        max_distance = distance
        farthest_object = obj

print(farthest_object)
print(f"{max_distance:.2f}")
