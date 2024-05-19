with open(input(), 'r') as file:
    numbers = [int(line.strip()) for line in file]

print(sum(numbers))
