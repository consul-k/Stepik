'''

Если присмотреться к 8-ной системе счисления, то можно проследить алгоритм получения восьмеричного числа из десятичного. 
Сможете ли вы его найти и перевести число из 10-ной системы в 8-ную без использования функции oct?

Ваша программа принимает на вход 10-ное число в интервале от 8 до 63 включительно. 
Напишите программу, которая переводит число из 10-ной системы в 8-ную систему счисления без использования oct. 
Программа должна вывести число в восьмеричном представлении.

Sample Input 1:

8

Sample Output 1:

10

Sample Input 2:

17

Sample Output 2:

21

Sample Input 3:

63

Sample Output 3:

77

'''

a = int(input())
n = a//8
print(int(a+2*n))
