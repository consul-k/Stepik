'''

Программа принимает на вход три символа через пробел в одну строку. Необходимо вывести код каждого символа при помощи функции ord в определенном формате.

Sample Input 1:

A , y

Sample Output 1:

Simvol code A is 65.
Simvol code , is 44.
Simvol code y is 121.

Sample Input 2:

q w e

Sample Output 2:

Simvol code q is 113.
Simvol code w is 119.
Simvol code e is 101.

'''

a, b, c= map(str, input().split())
print(f'Simvol code {a} is {ord(a)}.')
print(f'Simvol code {b} is {ord(b)}.')
print(f'Simvol code {c} is {ord(c)}.')
