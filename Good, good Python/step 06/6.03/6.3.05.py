'''

Подвиг 7. Вводятся целые числа в одну строку через пробел. На их основе формируется кортеж. 
Необходимо создать еще один кортеж с уникальными (не повторяющимися) значениями из первого кортежа. Результат отобразите в виде списка чисел через пробел.

P. S. Подобные задачи решаются, как правило, с помощью множеств, но в качестве практики пока обойдемся без них.

Sample Input:

8 11 -5 -2 8 11 -5

Sample Output:

8 11 -5 -2

'''

old_tuple = tuple(map(int, input().split()))
new_tuple = ()
for i in old_tuple:
    if i not in new_tuple:
        new_tuple += i,
print(*tuple(new_tuple))
