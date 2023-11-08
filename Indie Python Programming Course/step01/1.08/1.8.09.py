'''

Дано целое число n. Выведите следующее за ним четное число.

Задачу необходимо решить целочисленными операциями без использования условных операторов и\или циклов.

Sample Input 1:

5

Sample Output 1:

6

Sample Input 2:

6

Sample Output 2:

8

Sample Input 3:

401

Sample Output 3:

402

Sample Input 4:

163

Sample Output 4:

164

'''

a = int(input())
print((a//2+1)*2)
