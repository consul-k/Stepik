res = []

for i in range(int(input())):
    i = tuple(input().split(', '))
    if 'Главная роль' in i:
        res.append(i)

if res:
    print('Персонажи, играющие главную роль:')
    for j in res:
        print(j)
else:
    print('Персонажи отсутствуют')
