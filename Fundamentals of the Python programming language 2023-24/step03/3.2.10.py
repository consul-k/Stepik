line = input()
numbers = [int(s) for s in line.split()]

k = int(input())

filtered_numbers = [num for num in numbers if num % k != 0]

filtered_numbers.sort()

for num in filtered_numbers:
    print(num)
