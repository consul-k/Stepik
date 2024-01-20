'''

Подвиг 10. Вводятся пункты меню (каждый пункт с новой строки) в формате:

название_1 URL-адрес_1
название_2 URL-адрес_2
...
название_N URL-адрес_N

Необходимо эту информацию представить в виде вложенного кортежа menu в формате:

((название_1, URL-адрес_1), (название_2, URL-адрес_2), ... (название_N, URL-адрес_N))

Результат вывести на экран в виде кортежа командой:

print(menu)

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:

Главная home
Python learn-python
Java learn-java
PHP learn-php

Sample Output:

(('Главная', 'home'), ('Python', 'learn-python'), ('Java', 'learn-java'), ('PHP', 'learn-php'))

'''

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
t = []
for i in lst_in:
    t.append(tuple(i.split()))
print(tuple(t))
