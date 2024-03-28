numbers = input().split()
total = sum(int(num) for num in numbers)
print(" + ".join(numbers), "=", total)
