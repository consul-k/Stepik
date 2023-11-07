'''

Программа, считывает натуральное число n, после чего выводит двойное неравенство этого числа с его соседними числами.

Смотрите примеры ниже

Sample Input 1:

15

Sample Output 1:

14<15<16

Sample Input 2:

21

Sample Output 2:

20<21<22

Sample Input 3:

567

Sample Output 3:

566<567<568

'''

n = int(input())
print(n-1,'<',n,'<',n+1,sep='')
