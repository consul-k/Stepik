'''

На вход программе подаётся два целых числа a и b, каждое на новой строке.

Выведите в консоль строку вида: a\n + \nb\n = \nc, где a и  b - полученные числа, а c - их сумма.

Sample Input 1:

2
3

Sample Output 1:

2\n + \n3\n = \n5

Sample Input 2:

53
54

Sample Output 2:

53\n + \n54\n = \n107

Sample Input 3:

-5
5

Sample Output 3:

-5\n + \n5\n = \n0

'''

a, b = int(input()), int(input())
print(fr'{a}\n + \n{b}\n = \n{a+b}')
