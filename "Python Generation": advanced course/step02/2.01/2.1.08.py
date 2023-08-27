'''

n человек, пронумерованных числами от 1 до n, стоят в кругу. 
Они начинают считаться, каждый k-й по счету человек выбывает из круга, после чего счет продолжается со следующего за ним человека. 
Напишите программу, определяющую номер человека, который останется в кругу последним.

Формат входных данных
На вход программе подаются два числа n и k, записанные на отдельных строках.

Формат выходных данных
Программа должна вывести одно число – номер человека, который останется в кругу последним.

Примечание 1. Подробнее ознакомиться с классической задачей Иосифа Флавия можно тут.

Примечание 2. Визуализацию работы алгоритма можно посмотреть тут.
Тестовые данные 🟢

Sample Input 1:

2
1

Sample Output 1:

2

Sample Input 2:

5
2

Sample Output 2:

3

Sample Input 3:

7
5

Sample Output 3:

6

'''

n = int(input())
k = int(input())
s = 0

for i in range(1,n+1):
    s = (s + k) % i
print(s + 1)
