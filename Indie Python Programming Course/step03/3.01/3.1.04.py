'''

Программа получает на вход три натуральных числа A, B и C через пробел. 

Вам необходимо вывести YES в том случае, если A + B = C и вывести NO в противном случае.

Sample Input 1:

4 5 9

Sample Output 1:

YES

Sample Input 2:

1 2 4

Sample Output 2:

NO

'''

a,b,c = map(int, input().split())
if a+b==c:
    print('YES')
else:
    print('NO')
