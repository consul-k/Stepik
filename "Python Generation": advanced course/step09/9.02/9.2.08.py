'''

Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба этих предмета. 
У руководителя школы есть списки изучающих каждый предмет.

Напишите программу, позволяющую руководителю выяснить, сколько учеников изучает только один предмет.

Формат входных данных
На вход программе в первых двух строках подаются числа m и n – количества учеников, изучающих математику и информатику соответственно. 
Далее идут m строк — фамилии учеников, которые изучают математику и n строк с фамилиями учеников, изучающих информатику.

Формат выходных данных
Программа должна вывести количество учеников, которые изучают только один предмет. Если таких учеников не окажется, то необходимо вывести NO.

Примечание. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.
Тестовые данные 🟢

Sample Input 1:

5
4
Демин
Рыбаков
Сафонов
Игнатов
Мухин
Сафонов
Игнатов
Демин
Рыбаков

Sample Output 1:

1

Sample Input 2:

3
1
Петухов
Фокин
Самойлов
Фокин

Sample Output 2:

2

Sample Input 3:

2
4
Блинов
Жданов
Бобров
Жданов
Некрасов
Блинов

Sample Output 3:

2

'''

m = int(input())
n = int(input())
math = set()
inf = set()

for name in range(m):
    name = input()
    math.add(name)
for name in range(n):
    name = input()
    inf.add(name)
    
only_one = math ^ inf
if not only_one:
    print('NO')
else:
    print(len(only_one))
