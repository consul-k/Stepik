'''

Дан большой текст, который состоит из нескольких строк, он находится в переменной text.

Найдите в нём текст от start до end.
Что нужно сделать:

Нужно найти весь текст от start до end, текст может быть растянут на несколько строк.
Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Найденный текст.

Sample Input 1:

start
Каждое
Слово
На
Новой
Строке
end

Sample Output 1:

['\nКаждое\nСлово\nНа\nНовой\nСтроке\n']

Sample Input 2:

spamstartЭТОТ
ТЕКСТ
НАХОДИТСЯ
НА
НЕСКОЛЬКИХ
СТРОКАХ
endspam

Sample Output 2:

['ЭТОТ\nТЕКСТ\nНАХОДИТСЯ\nНА\nНЕСКОЛЬКИХ\nСТРОКАХ\n']

Sample Input 3:

start тут нету завершения,
программа не должна что-то выводить

Sample Output 3:

[]

'''

import re, sys


text = ''.join(sys.stdin.readlines())
result = re.findall(r'(?s)(?<=start)(.*)(?=end)', text)
print(result)
