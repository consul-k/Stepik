line = input()
numbers = [int(s) for s in line.split()]

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        print(numbers[i])
