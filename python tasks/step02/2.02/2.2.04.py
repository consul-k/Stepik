numbers = list(map(int, input().split()))

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

max_frequency = max(frequency.values())
most_frequent_numbers = [num for num, freq in frequency.items() if freq == max_frequency]

result = max(most_frequent_numbers)

print(result)
