'''

Сортировка подсчетом

Как видно из названия задачи, вам необходимо отсортировать список, состоящий только из чисел в пределах от -100 до 100 включительно, сортировкой подсчетом.

Программа получает на вход число n - количество элементов в списке, затем сами элементы списка

Вам необходимо вывести отсортированный список

P.S. не пользуйтесь встроенной функцией sorted или методом sort

Sample Input 1:

5
8 9 8 7 2

Sample Output 1:

2 7 8 8 9

Sample Input 2:

7
-8 5 -7 4 -8 0 4

Sample Output 2:

-8 -8 -7 0 4 4 5

Sample Input 3:

8
66 -66 -48 -96 -17 -80 -57 -45

Sample Output 3:

-96 -80 -66 -57 -48 -45 -17 66

Sample Input 4:

50
25 -25 -85 -86 -66 71 29 55 3 100 82 64 -80 65 -7 24 40 -92 47 -45 37 50 -75 27 -9 -24 43 76 -1 82 61 -32 -11 85 -95 77 -96 47 -48 -34 -28 -86 81 93 -17 60 -46 42 2 60

Sample Output 4:

-96 -95 -92 -86 -86 -85 -80 -75 -66 -48 -46 -45 -34 -32 -28 -25 -24 -17 -11 -9 -7 -1 2 3 24 25 27 29 37 40 42 43 47 47 50 55 60 60 61 64 65 71 76 77 81 82 82 85 93 100

'''

n = int(input())
list_number = list(map(int, input().split()))
numbers = []

for i in range(-100, 101):
    for a in list_number:
        if i == a:
            numbers.append(i)
print(*numbers)
