numbers = input().split()
numbers = [int(num) for num in numbers]
min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))
numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
print(*numbers)
