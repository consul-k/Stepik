line_a = input()
list_a = [int(s) for s in line_a.split()]
line_b = input()
list_b = [int(s) for s in line_b.split()]

# напишите ваше решение здесь
for i in list_a:
    if i not in list_b:
        print(i)
