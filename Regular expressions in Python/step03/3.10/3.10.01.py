'''

Удалите все знаки препинания из текста и выведите количество совершённых замен.
Что нужно сделать:

Нужно удалить все знаки препинания в тексте: .?!,:.
Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Количество совершённых замен.

Sample Input 1:

Через час те из вас, кто останется в живых, будут завидовать мёртвым.

Sample Output 1:

3

Sample Input 2:

Maybe it’s my fault. Maybe I led you to believe it was easy, when it wasn’t. Maybe I made you think my highlights started at the free throw line, and not in the gym. Maybe I made you think that every shot I took was a game winner. That my game was built on flash, and not fire. Maybe it’s my fault that you didn’t see that failure gave me strength, that my pain was my motivation. Maybe I led you to believe that basketball was a God given gift, and not something I worked for, every single day of my life.

Sample Output 2:

13

'''

import re

result = re.subn(r'[.?!,:.]', '', input())
print(result[-1])
