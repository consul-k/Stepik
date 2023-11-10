'''

Вводятся два целых числа, каждое в отдельной строке.

Ваша задача вывести наибольшее из данных чисел.

Примечание: используйте только условный оператор, функцией max пользоваться нельзя

Sample Input 1:

8
11

Sample Output 1:

11

Sample Input 2:

50
21

Sample Output 2:

50

'''

a, b = int(input()), int(input())
if a>b:
    print(a)
else:
    print(b)
