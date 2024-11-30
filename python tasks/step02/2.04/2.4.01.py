input_data = input()

elements = input_data.split()

numbers = [x for x in elements if x.isdigit()]
words = [x for x in elements if not x.isdigit()]

print(" ".join(numbers))
print(" ".join(words))
