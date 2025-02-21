n, k = map(int, input().split())
t = 240
count = 5
z = 0
while t - k >= count and z < n:
    t -= count
    count += 5
    z += 1
print(z)
