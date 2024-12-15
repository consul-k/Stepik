def count_elements_greater_than_neighbors(numbers):
    count = 0
    for i in range(1, len(numbers) - 1):
        if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
            count += 1
    return count

numbers = list(map(int, input().split()))
result = count_elements_greater_than_neighbors(numbers)
print(result)
