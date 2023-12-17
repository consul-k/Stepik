'''

В файле https://stepik.org/media/attachments/lesson/209723/3.html находится одна таблица. 
Просуммируйте все числа в ней и введите в качестве ответа одно число - эту сумму. Для доступа к ячейкам используйте возможности BeautifulSoup.

'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/209723/3.html')
html = resp.read().decode('utf8')
soup = BeautifulSoup(html, 'html.parser')

cnt = 0
for tr in soup.find_all('tr'):
    for td in tr.find_all(['td', 'th']):
        cnt += int(td.text)
print(cnt)
