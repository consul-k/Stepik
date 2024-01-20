'''

Подвиг 6. Вводятся данные в формате:

<день рождения 1> имя_1
<день рождения 2> имя_2
...
<день рождения N> имя_N

Дни рождений и имена могут повторяться. На их основе сформировать словарь и вывести его в формате (см. пример ниже):

день рождения 1: имя1, ..., имяN1
день рождения 2: имя1, ..., имяN2
...
день рождения M: имя1, ..., имяNM

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:

3 Сергей
5 Николай
4 Елена
7 Владимир
5 Юлия
4 Светлана

Sample Output:

3: Сергей
5: Николай, Юлия
4: Елена, Светлана
7: Владимир

'''

import sys
lst_in = [i.split() for i in list(map(str.strip, sys.stdin.readlines()))]
d = {}
for i in lst_in:
    if i[0] not in d:
        d[i[0]] = [i[1]]
    else:
        d[i[0]].append(i[1])
for k, v in d.items():
    print(k + ": "+", ".join(v))
