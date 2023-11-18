'''

Cтрока S1 называется анаграммой строки S2, если она получается из S2 перестановкой символов.

Программа получает на вход две строки S1 и S2. Если строка S1 является анаграммой строки S2 нужно вывести YES, в противном случае - NO

Sample Input 1:

abc
cba

Sample Output 1:

YES

Sample Input 2:

abracadabra
cadabraabra

Sample Output 2:

YES

Sample Input 3:

abb
bbc

Sample Output 3:

NO

'''

a, b = input(), input()
a1 = {}
b1 = {}
for i in a:
    a1[i] = a.count(i)
for i in b:
    b1[i] = b.count(i)
if a1 == b1:
    print('YES')
else:
    print('NO')
