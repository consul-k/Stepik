line = input()
numbers = [int(s) for s in line.split()]

# напишите ваше решение здесь
lst1 = []
for i in numbers:
    if i not in lst1:
        lst1.append(i)
print(len(lst1))
