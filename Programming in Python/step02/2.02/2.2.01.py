'''

Напишите программу, которая считывает целые числа с консоли по одному числу в строке.

Для каждого введённого числа проверить:
если число меньше 10, то пропускаем это число;
если число больше 100, то прекращаем считывать числа;
в остальных случаях вывести это число обратно на консоль в отдельной строке.

Sample Input 1:

12
4
2
58
112

Sample Output 1:

12
58

Sample Input 2:

101

Sample Output 2:

Sample Input 3:

1
2
102

Sample Output 3: 

'''

a = 0
while a < 101:
    a = int(input())
    if a >= 10 and a <= 100:
        print(a)
    if a > 100:
        break
else:
    print(a)
