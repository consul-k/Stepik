'''

Подвиг 5. Вводятся целые числа в одну строчку через пробел. 
Необходимо преобразовать эти данные в список целых чисел. 
Затем, перебрать этот список в цикле for и просуммировать все нечетные значения. Результат вывести на экран.

Sample Input:

8 11 -2 4 0 13 19 12 7

Sample Output:

50

'''

lst = map(int, input().split())
res = 0
for i in lst:
    if i%2!=0:
        res += i
print(res)
