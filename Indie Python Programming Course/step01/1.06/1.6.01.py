'''

Напишите программу, которая вычисляет среднее арифметическое четырех введенных целых чисел.

Обратите внимание, что числа вводятся в одну строку через пробел
🚀>P.S.: Подсказка для решения 🚀

Sample Input 1:

2 3 4 5

Sample Output 1:

3.5

Sample Input 2:

3 3 4 4

Sample Output 2:

3.5

Sample Input 3:

5 3 4 5

Sample Output 3:

4.25

'''

a,b,c,d = map(int,input().split())
print((a+b+c+d)/4)
