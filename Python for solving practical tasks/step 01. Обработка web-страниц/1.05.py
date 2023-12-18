'''

В файле https://stepik.org/media/attachments/lesson/209723/5.html находится одна таблица. Просуммируйте все числа в ней. 
Теперь мы не только добавили разных тегов для изменения стиля отображения, но и сделали невалидный HTML-код 
(правда, браузеры его отображают, а вот с BeautifulSoup могут быть проблемы). Невалидный HTML-код - не редкость в интернете, надо учиться работать и с этим.

Вы можете исправить html-код или попробовать использовать нестандартный парсер html, такой как html5lib.

'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/209723/5.html')
html = resp.read().decode('utf8')
soup = BeautifulSoup(html, 'html.parser')

cnt = 0
for tr in soup.find_all('tr'):
    for td in tr.find_all(['td', 'th']):
        cnt += int(td.text)
print(cnt)
