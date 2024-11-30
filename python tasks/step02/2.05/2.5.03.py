numbers = input()

positive_numbers = [int(num) for num in numbers.split() if int(num) > 0]

print(" ".join(map(str, positive_numbers)))
