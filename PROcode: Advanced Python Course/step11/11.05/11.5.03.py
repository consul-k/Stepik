N = int(input())

robots = []
for _ in range(N):
    data = input().split()
    robots.append((int(data[0]), int(data[1])))

robots = list(map(lambda robot: (robot[0], robot[1] * 1.2), robots))

robots = list(filter(lambda robot: robot[1] >= 100, robots))

robots = sorted(robots, key=lambda robot: robot[0])

result = list(map(lambda robot: (robot[0], round(robot[1], 2)), robots))

print(result)
