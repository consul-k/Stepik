'''

В этой задаче вам предстоит построить лесенку из чисел. 
Программа принимает на вход целое положительное число n (n<=15) - количество уровней, ваша задача вывести n уровней, 
в каждом из которых стоят числа от 1 до значения уровня.

Sample Input 1:

2

Sample Output 1:

1
1 2

Sample Input 2:

3

Sample Output 2:

1
1 2
1 2 3

'''

n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep='', end=' ')
    print()
