'''

Подвиг 2. Вводятся два списка целых чисел каждый с новой строки (в строке наборы чисел через пробел). 
Необходимо выбрать и отобразить на экране уникальные числа, присутствующие в первом списке, но отсутствующие во втором. 
Результат выведите на экран в виде строки чисел, записанных по возрастанию через пробел.

Sample Input:

8 5 3 5 -3 1
1 2 3 4

Sample Output:

-3 5 8

'''

# put your python code here
a = set(map(int, input().split()))
b = set(map(int, input().split()))
s = a-b
print(*sorted(s))
