'''

Даны два списка чисел. Выведите все числа в порядке возрастания, которые входят в первый список, но при этом отсутствуют во втором. 

Sample Input:

1 3 2 5
4 3 2 6

Sample Output:

1 5

'''

a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = sorted(a - b)
print(*c)
