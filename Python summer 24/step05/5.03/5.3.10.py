input_string = input()

frequency = {}

for char in input_string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

most_common_char = max(frequency, key=lambda k: (frequency[k], k))

print(most_common_char)
