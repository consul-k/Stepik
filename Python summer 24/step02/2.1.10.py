N = int(input())
M = int(input())
X = int(input())
Y = int(input())

min_distance = min(X, N - X, Y, M - Y)

print(min_distance)
