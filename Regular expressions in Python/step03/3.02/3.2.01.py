'''

В переменной match записан объект Match. Выведите на экран:

    Его нулевую группу
    Начало вхождения нулевой группы
    Конец вхождения нулевой группы
    Атрибут pos
    Атрибут endpos
    Атрибут re
    Атрибут string

На входные данные и функцию re.match() не обращайте внимания.

Sample Input 1:

I
I love regex!

Sample Output 1:

I
0
1
0
13
re.compile('I')
I love regex!

Sample Input 2:

\b[А-Яа-я]+\b
Второй тест

Sample Output 2:

Второй
0
6
0
11
re.compile('\\b[А-Яа-я]+\\b')
Второй тест

'''

import re

match = re.match(input(), input())

print(match.group())
print(match.start())
print(match.end()) 
print(match.pos)
print(match.endpos)
print(match.re)
print(match.string)
