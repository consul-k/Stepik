'''

Напишите программу, которая получает на вход число, представленное в 6-чной системе счисления и переводит его в 16-чную систему. 
Ваша программа должна вывести результат в 16-чной системе.

Sample Input 1:

1124

Sample Output 1:

0x10c

Sample Input 2:

555

Sample Output 2:

0xd7

Sample Input 3:

0

Sample Output 3:

0x0

'''

a = input()
b = (int(a, 6))
print(hex(b))
