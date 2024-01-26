'''

Подвиг 6. Имеется словарь, содержащий пункты меню:

menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}

Дополнительно вводятся еще пункты меню в виде строк в формате:

название_1=url_1
...
название_N=url_N

Необходимо эту введенную информацию преобразовать в словарь и добавить к словарю menu, используя оператор распаковки для словарей. 
На результирующий словарь должна вести переменная menu. Выводить словарь не нужно, только сформировать.

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:

Города=about-cities
Машины=read-of-cars
Самолеты=airplanes

Sample Output:

Архив Главная Города Машины Новости Самолеты
about-cities airplanes archive home news read-of-cars

'''

import sys

# считывание списка из входного потока
lst_in = dict([(*i.rstrip('\n').split('='),) for i in sys.stdin.readlines()])

menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# здесь продолжайте программу (используйте список lst_in и menu)
menu = {**menu, **lst_in}
