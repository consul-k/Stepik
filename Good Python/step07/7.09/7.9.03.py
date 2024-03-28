numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
n = int(input())
for _ in range(n):
    ai = int(input())
    print(numbers[ai - 1])
