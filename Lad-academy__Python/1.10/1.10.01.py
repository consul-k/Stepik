numbers = input().split()

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

most_frequent_number = None
max_frequency = 0

for number, count in frequency.items():
    if count > max_frequency:
        max_frequency = count
        most_frequent_number = number

print(most_frequent_number)
