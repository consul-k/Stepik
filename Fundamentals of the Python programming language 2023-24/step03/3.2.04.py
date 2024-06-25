line = input()
numbers = [int(s) for s in line.split()]

# напишите ваше решение здесь
for num in numbers:
    if num < 0:
        print(num)
