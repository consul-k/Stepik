'''

Подвиг 8. Вводятся номера телефонов в формате:

номер_1 имя_1
номер_2 имя_2
...
номер_N имя_N

Необходимо создать словарь d, где ключами будут имена, а значениями - список номеров телефонов для этого имени. 
Обратите внимание, что одному имени может принадлежать несколько разных номеров. Полученный словарь вывести командой:

print(*sorted(d.items()))

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:

+71234567890 Сергей
+71234567810 Сергей
+51234567890 Михаил
+72134567890 Николай

Sample Output:

('Михаил', ['+51234567890']) ('Николай', ['+72134567890']) ('Сергей', ['+71234567890', '+71234567810'])

'''

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
d = {}
lst_in = [i.split() for i in lst_in]
for i in lst_in:
    if i[-1] not in d:
        d[i[-1]] = [i[0]]
    else:
        d[i[-1]].append(i[0])

print(*sorted(d.items()))
