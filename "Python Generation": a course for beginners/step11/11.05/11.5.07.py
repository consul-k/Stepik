input_string = input()

numbers = list(map(int, input_string.split()))

pairs_count = 0

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            pairs_count += 1

print(pairs_count)
