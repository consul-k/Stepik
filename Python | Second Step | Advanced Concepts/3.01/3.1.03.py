numbers = list(map(int, input().split()))
indexes = list(map(int, input().split()))

for i in indexes:
    numbers[i] = round(numbers[i] * 1.1, 1)

print("Измененный список:", numbers)
