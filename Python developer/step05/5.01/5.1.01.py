'''

Допишите программу так, чтобы она выводила получаемый на вход список чисел из переменной a.

Sample Input 1:

1 2 3 4

Sample Output 1:

1
2
3
4

Sample Input 2:

123 321 454 545 1

Sample Output 2:

123
321
454
545
1

'''

a = [int(i) for i in input().split()] # [1,2,3,4]
for i in a:
    print(i)
