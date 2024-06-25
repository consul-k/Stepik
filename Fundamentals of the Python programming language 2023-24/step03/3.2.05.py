line = input()
numbers = [int(s) for s in line.split()]

# напишите ваше решение здесь
res = 0
for num in numbers:
    if num > 0:
        res += 1
print(res)
