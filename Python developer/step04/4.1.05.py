'''

Пользователь вводит два целых числа a и b. Выведите меньшее из них.

Sample Input 1:

8
9

Sample Output 1:

8

Sample Input 2:

-10
10

Sample Output 2:

-10

Sample Input 3:

20
10

Sample Output 3:

10

Sample Input 4:

5
6

Sample Output 4:

5

Sample Input 5:

1
2

Sample Output 5:

1

Sample Input 6:

0
0

Sample Output 6:

0

Sample Input 7:

1
1

Sample Output 7:

1

Sample Input 8:

30
-20

Sample Output 8:

-20

Sample Input 9:

-20
30

Sample Output 9:

-20

Sample Input 10:

-8
-5

Sample Output 10:

-8

'''

a, b = int(input()), int(input())
if a < b:
    print(a)
else:
    print(b)
