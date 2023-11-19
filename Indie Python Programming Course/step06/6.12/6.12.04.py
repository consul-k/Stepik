'''

Вашей программе будут поступать на вход N списков, содержащих целые числа

Ваша задача определить сколько всего встречалось различных чисел во всех этих списках

Входные данные

Сперва поступает натуральное число N - количество списков

В следующих N строк вводятся значения каждого списка, разделенные через пробел

Выходные данные

Вывести одно число - количество различных чисел во всех этих списках

Sample Input 1:

2
1 2 3 2 1 4
1 1 2 2 2

Sample Output 1:

4

Sample Input 2:

4
1
1 2 3
1 2 3 4 4 4 3 4 1 2
123 1000 800 123

Sample Output 2:

7

Sample Input 3:

3
1 2 3 4 5
4 5 6
5 6 7 8

Sample Output 3:

8

'''

l = set()
for i in range(int(input())):
    i = set(map(int, input().split()))
    l.update(i)
print(len(l))
