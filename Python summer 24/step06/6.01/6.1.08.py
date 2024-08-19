n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

result = []

for i in range(1, n):
    if arr[i] > arr[i-1]:
        result.append(arr[i])

result.sort()

if result:
    print(*result)
else:
    print("NO")
