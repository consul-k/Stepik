'''

В файле https://stepik.org/media/attachments/lesson/209723/4.html находится одна таблица. 
Просуммируйте все числа в ней. Теперь мы добавили разных тегов для изменения стиля отображения. Для доступа к ячейкам используйте возможности BeautifulSoup.

'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/209723/4.html')
html = resp.read().decode('utf8')
soup = BeautifulSoup(html, 'html.parser')

cnt = 0
for tr in soup.find_all('tr'):
    for td in tr.find_all(['td', 'th']):
        cnt += int(td.text)
print(cnt)
