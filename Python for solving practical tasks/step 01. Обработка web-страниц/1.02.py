'''

Файл https://stepik.org/media/attachments/lesson/209719/2.html содержит статью с Википедии про язык Python. 
В этой статье есть теги code, которыми выделяются конструкции на языке Python. В
ам нужно найти все строки, содержащиеся между тегами <code> и </code> и найти те строки, которые встречаются чаще всего и вывести их в алфавитном порядке, 
разделяя пробелами.

Например, если исходный текст страницы выглядел бы так:

<code>a</code>
<a>bracadabr</a>
<code>c</code>
<code>b</code>
<code>b</code>
<code>c</code>

то в ответ надо было бы ввести строку "b c".

'''

import re
from urllib.request import urlopen
from collections import Counter

html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
page = str(html)

res = re.findall(r'<code>(\S*)</code>', page)
c = Counter(res)
print(c.most_common())
