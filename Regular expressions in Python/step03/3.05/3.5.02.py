'''

Проверьте пароль на валидность.
Что нужно сделать:

Проверить пароль на валидность. Валидным будем считать пароль, который:

    Состоит из a-z, A-Z, 0-9, @#$%^&*()_-+!?
    Его длина минимум 8 символов

Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Если это валидный пароль - выводите True, иначе - False.

Sample Input 1:

d2D8dh8DA#!

Sample Output 1:

True

Sample Input 2:

g0JDQ0#(dka02b vp

Sample Output 2:

False

Sample Input 3:

Это не пароль

Sample Output 3:

False

Sample Input 4:

111111111$%^1111111111

Sample Output 4:

True

Sample Input 5:

@#$%^64&*()_-+!?

Sample Output 5:

True

'''

import re

result = re.fullmatch('[0-9a-zA-Z\@\#\$\%\^\&\*\(\)\_\-\+\!\?]{8,}', input())
print(bool(result))
