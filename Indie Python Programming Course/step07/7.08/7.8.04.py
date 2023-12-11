'''

Описать рекурсивную функцию double_fact, которая принимает на вход целое число и вычисляет значение двойного факториала по формуле:

double_fact(7) => 105
double_fact(4) => 8
double_fact(1) => 1
double_fact(10) => 3840

Ваша задача только написать определение функции double_fact

Sample Input 1:

6

Sample Output 1:

48

Sample Input 2:

5

Sample Output 2:

15

Sample Input 3:

2

Sample Output 3:

2

Sample Input 4:

4

Sample Output 4:

8

'''

def double_fact(n):
    if n < 3:
        return n
    return double_fact(n - 2) * n
