'''

Подвиг 10. Тестовый веб-сервер возвращает HTML-страницы по URL-адресам (строкам). 
На вход программы поступают различные URL-адреса. Если адрес пришел впервые, то на экране отобразить строку (без кавычек):

"HTML-страница для адреса <URL-адрес>"

Если адрес приходит повторно, то следует взять строку "HTML-страница для адреса <URL-адрес>" из словаря и вывести на экран сообщение (без кавычек):

"Взято из кэша: HTML-страница для адреса <URL-адрес>"

Сообщения выводить каждое с новой строки.

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:

ustanovka-i-zapusk-yazyka
ustanovka-i-poryadok-raboty-pycharm
peremennyye-operator-prisvaivaniya-tipy-dannykh
arifmeticheskiye-operatsii
ustanovka-i-poryadok-raboty-pycharm

Sample Output:

HTML-страница для адреса ustanovka-i-zapusk-yazyka
HTML-страница для адреса ustanovka-i-poryadok-raboty-pycharm
HTML-страница для адреса peremennyye-operator-prisvaivaniya-tipy-dannykh
HTML-страница для адреса arifmeticheskiye-operatsii
Взято из кэша: HTML-страница для адреса ustanovka-i-poryadok-raboty-pycharm

'''

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)

x = []
for i in lst_in:
    if i in x:
        print(f'Взято из кэша: HTML-страница для адреса {i}')
    else:
        print(f'HTML-страница для адреса {i}')
    x.append(i) 
