'''

Мы сохранили страницу с википедии про языки программирования и сохранили по адресу https://stepik.org/media/attachments/lesson/209717/1.html

Скачайте её с помощью скрипта на Питоне и посчитайте, какой язык упоминается чаще Python или C++ (ответ должен быть одной из этих двух строк).

'''

from urllib.request import urlopen
html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8')
page = str(html)
python_count = (html.count('Python'))
c_count = (html.count('C++'))
if python_count > c_count:
    print('Python')
else:
    print('C++')
