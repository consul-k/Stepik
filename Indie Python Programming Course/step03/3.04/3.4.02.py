'''

Даны три целых числа, записанных в отдельных строках. Определите, сколько среди них совпадающих.

Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадают) или 0 (если все числа различны).

Разбор решения Youtube Patreon Boosty

Sample Input 1:

6
6
6

Sample Output 1:

3

Sample Input 2:

7
8
7

Sample Output 2:

2

'''

a=int(input())
b=int(input())
c=int(input())
if(a==b and b==c):
    print(3)
elif a==b or b==c or a==c:
    print(2)
else:
    print(0)
