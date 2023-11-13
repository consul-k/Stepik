'''

Программа получает на вход натуральное число N. 

Нужно найти сумму его делителей. 

Sample Input 1:

10

Sample Output 1:

18

Sample Input 2:

31

Sample Output 2:

32

'''

n = int(input())
i = 1
l = []
while i <= n:
    if n%i==0:
        l.append(i)
    i += 1
print(sum(l))
