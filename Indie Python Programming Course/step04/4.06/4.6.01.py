'''

Программа получает на вход натуральное число n > 1. Выведите минимальный делитель этого числа, отличный от единицы.

К примеру для числа 12 делителями являются 1, 2, 3, 4, 6, 12. 

Sample Input 1:

12

Sample Output 1:

2

Sample Input 2:

15

Sample Output 2:

3

Sample Input 3:

7

Sample Output 3:

7

'''

n = int(input())
i = 2
l = []
while n >= i:
    if n % i == 0:
        l.append(i)
    i += 1
print(min(l))
