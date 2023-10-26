'''

Вашему серверу на вход прилетает IP-адрес (v4) клиента. Нужно определить, что IP-адрес – правильный.

IP-адрес (v4) считается правильным, когда его размер составляет 4 байта и состоит он из 4-х цифр. 
На каждую цифру приходится 1 байт, и следовательно максимальное число, которое там помещается – 255, а минимальное 0.

Условия:

    Каждая цифра находится в интервале от 0 до 255 включительно.
    IP адрес не может быть 0.0.0.0 или 255.255.255.255, так как они зарезервированы для специального назначения.

На вход вашей программе поступают 4 целых неотрицательных числа, разделенных точкой n1, n2, n3, n4 – они уже введены в программу, снова вводить их не нужно!

В качестве ответа выведите True если IP-адрес правильный или False если неправильный.

Sample Input 1:

127.0.0.1

Sample Output 1:

True

Sample Input 2:

0.0.0.0

Sample Output 2:

False

Sample Input 3:

255.255.255.255

Sample Output 3:

False

Sample Input 4:

192.234.43.23

Sample Output 4:

True

Sample Input 5:

1.0.0.0

Sample Output 5:

True

Sample Input 6:

256.0.0.1

Sample Output 6:

False

Sample Input 7:

0.256.0.0

Sample Output 7:

False

Sample Input 8:

0.0.256.0

Sample Output 8:

False

Sample Input 9:

0.0.0.256

Sample Output 9:

False

Sample Input 10:

0.255.255.255

Sample Output 10:

True

Sample Input 11:

255.0.0.0

Sample Output 11:

True

Sample Input 12:

0.255.0.0

Sample Output 12:

True

Sample Input 13:

255.0.255.255

Sample Output 13:

True

Sample Input 14:

0.0.255.0

Sample Output 14:

True

Sample Input 15:

255.255.0.255

Sample Output 15:

True

Sample Input 16:

0.0.0.255

Sample Output 16:

True

Sample Input 17:

255.255.255.0

Sample Output 17:

True

'''

n1, n2, n3, n4 = [int(i) for i in input().split('.')]
if n1 == n2 == n3 == n4 == 0 or n1 == n2 == n3 == n4 == 255:
    print('False')
else:
    print(0<=n1<=255 and 0<=n2<=255 and 0<=n3<=255 and 0<=n4<=255)
