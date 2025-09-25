s = set(input())
res = [i for i in s if i.isdigit()]
if len(res) == 0:
    print('Цифр нет')
else:
    print(*sorted(res))
