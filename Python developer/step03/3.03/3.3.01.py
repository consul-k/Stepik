'''

Напишите программу, которая переведет десятичное число, которое дается на вход вашей программе, в 2, 8 и 16 системы счисления. 
В качестве ответа выведите представление числа в этих системах счисления.

Sample Input 1:

17

Sample Output 1:

0b10001
0o21
0x11

Sample Input 2:

123

Sample Output 2:

0b1111011
0o173
0x7b

Sample Input 3:

0

Sample Output 3:

0b0
0o0
0x0

'''

a = int(input())
print(bin(a))
print(oct(a))
print(hex(a))
