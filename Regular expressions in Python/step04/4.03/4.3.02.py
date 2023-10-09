'''

Разделите строку по символам ? и &.
Что нужно сделать:

Нужно разделить строку по символвам ? и &, оставив эти символы в полученном списке.
Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Список, с частями исходной строки.

Sample Input 1:

https://stackoverflow.com/questions/tagged/regex?tab=votes&page=11&pagesize=15

Sample Output 1:

['https://stackoverflow.com/questions/tagged/regex', '?', 'tab=votes', '&', 'page=11', '&', 'pagesize=15']

Sample Input 2:

https://www.youtube.com/results?search_query=random+stream&sp=EggIARABGAFAAQ%253D%253D

Sample Output 2:

['https://www.youtube.com/results', '?', 'search_query=random+stream', '&', 'sp=EggIARABGAFAAQ%253D%253D']

'''

import re

result = re.split(r'([?&])', input())
print(result)
