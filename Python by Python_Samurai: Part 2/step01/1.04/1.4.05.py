import sys
lst = sys.stdin.readlines()
lst = [i.rstrip().split() for i in lst]       

# продолжите решение здесь(в lst храняться данные с которыми вы будете работать)
white = []
colored = []

for i, item in enumerate(lst):
    if item[1] == "б":
        white.append(item[0])
    else:
        colored.append(item[0])

print(white)
print(colored)
