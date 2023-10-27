'''

Вашей программе на вход поступает два числа a и b. Выведите числа от a до b включительно, чередуя у них знак. Например, для чисел 5 и 10 нужно вывести: 

5
-6
7
-8
9
-10

У границы a знак остается такой же какой и был. 0 в чередование знаков включается.

Sample Input 1:

5
10

Sample Output 1:

5
-6
7
-8
9
-10

Sample Input 2:

1
2

Sample Output 2:

1
-2

Sample Input 3:

-5
5

Sample Output 3:

-5
4
-3
2
-1
0
1
-2
3
-4
5

Sample Input 4:

5
-5

Sample Output 4:

Sample Input 5:

1
3

Sample Output 5:

1
-2
3

Sample Input 6:

-2
2

Sample Output 6:

-2
1
0
-1
2

'''

a, b = int(input()), int(input())
k=1

for i in range(a,b+1):
    k *= -1
    print(-i*k)
