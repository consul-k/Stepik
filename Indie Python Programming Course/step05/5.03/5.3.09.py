'''

Для делимости числа на 11 необходимо, чтобы разность между суммой цифр, стоящих на четных местах, и суммой цифр, стоящих на нечетных местах, делилась на 11.

Требуется написать программу, которая проверит делимость заданного числа на 11.
Входные данные

Программа получает на вход одно натуральное число N, делимость которого надо проверить (1 ≤ N ≤ 1010000).
Выходные данные

Выведите “YES”, если число делится на 11, или “NO” иначе.

Разбор задачи Youtube Patreon Boosty

Sample Input 1:

1211

Sample Output 1:

NO

Sample Input 2:

143

Sample Output 2:

YES

Sample Input 3:

87635064

Sample Output 3:

YES

Sample Input 4:

87635063

Sample Output 4:

NO

'''

num = int(input())
lst = [int(i) for i in str(num)]

for i in lst:
    b = lst[::2]
    g = lst[1::2]

g = sum(b) - sum(g)

if g % 11 == 0:
    print("YES")
else:
    print("NO")
