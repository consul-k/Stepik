'''

На вход вашей программе поступает два неравных друг другу целых числа в отдельных строках

Ваша задача сохранить наименьшее из этих чисел в переменную  minimum, а наибольшее - в maximum

    Использовать нужно, конечно же, тернарный оператор

В качестве ответа выведите через пробел сперва minimum , а потом maximum

Sample Input 1:

8
11

Sample Output 1:

8 11

Sample Input 2:

900
800

Sample Output 2:

800 900

Sample Input 3:

-4
-3

Sample Output 3:

-4 -3

'''

a, b = int(input()), int(input())
minimum = a if a < b else b
maximum = a if a > b else b
print(minimum, maximum)
