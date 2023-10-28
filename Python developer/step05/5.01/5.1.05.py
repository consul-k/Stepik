'''

Вашей программе на вход поступает натуральное число n. Вам нужно сделать из чисел обратную пирамидку, например для числа 5 вывод будет следующим:

5 4 3 2 1
5 4 3 2
5 4 3
5 4
5

Sample Input 1:

5

Sample Output 1:

5 4 3 2 1
5 4 3 2
5 4 3
5 4
5

Sample Input 2:

1

Sample Output 2:

1

Sample Input 3:

2

Sample Output 3:

2 1
2

Sample Input 4:

3

Sample Output 4:

3 2 1
3 2
3

'''

n = int(input())
s = 0
for _ in range(n):
    for k in range(n, s, -1):
        print(k, end=' ')
    s += 1
    print()
