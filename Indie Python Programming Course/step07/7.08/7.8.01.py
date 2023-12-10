'''

Определите функцию print_from, которая принимает одно натуральное число n и распечатывает на экране убывающую последовательность целых чисел от n до 1
включительно. Каждое число необходимо выводить на отдельной строке. 

Ваша задача только написать определение функции print_from

Sample Input 1:

4

Sample Output 1:

4
3
2
1

Sample Input 2:

7

Sample Output 2:

7
6
5
4
3
2
1

Sample Input 3:

2

Sample Output 3:

2
1

'''

def print_from(n: int) -> None:
    print(n)
    if n == 1:
        return n
    print_from(n-1)
