N = int(input())
numbers = set(map(int, input().split()))

for num in range(1, N + 1):
    if num not in numbers:
        print(num, end=' ')
