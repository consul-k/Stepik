'''

Подвиг 3. Вводятся данные в формате ключ=значение в одну строчку через пробел. 
Значениями здесь являются целые числа (см. пример ниже). Необходимо на их основе создать словарь d с помощью функции dict() и вывести его на экран командой:

print(*sorted(d.items()))

Sample Input:

one=1 two=2 three=3

Sample Output:

('one', 1) ('three', 3) ('two', 2)

'''

lst_in = [j.split('=') for j in [i for i in input().split()]]
lst_in = [[i[0], int(i[-1])] for i in lst_in]
d = dict(lst_in)
print(*sorted(d.items()))
