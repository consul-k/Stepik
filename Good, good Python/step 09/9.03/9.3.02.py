'''

Подвиг 2. На вход поступает строка из целых чисел, записанных через пробел. 
С помощью функции map преобразовать эту строку в список целых чисел, взятых по модулю. 
Сформируйте именно список lst из таких чисел. Отобразите его на экране в виде набора чисел, идущих через пробел.

Sample Input:

-5 6 8 11 -10 0

Sample Output:

5 6 8 11 10 0

'''

s = list(map(int, input().split()))
b = list(map(abs,s))
print(*b)
