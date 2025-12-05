n = int(input())

coordinates = []

for _ in range(n):
    line = input().strip()
    zone = list(map(int, line.split()))
    coordinates.append(zone)

print(coordinates)

if n >= 2:
    print(f"Координата [1][0]: {coordinates[1][0]}")
else:
    print("Недостаточно зон для доступа к [1][0]")

max_sum = -float('inf')
max_zone = None

for zone in coordinates:
    zone_sum = sum(zone)
    if zone_sum > max_sum:
        max_sum = zone_sum
        max_zone = zone

print(f"Зона с максимальной суммой: {max_zone}")

max_point = -float('inf')
for zone in coordinates:
    for point in zone:
        if point > max_point:
            max_point = point

print(f"Максимальная координата: {max_point}")
