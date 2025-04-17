numbers = list(map(int, input().split()))

is_strictly_decreasing = all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))

print(is_strictly_decreasing)
