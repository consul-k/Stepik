'''

Исправьте код так, чтобы он заменил все буквы O на X. Новая буква должна быть такого же регистра, как и оригинальная.

Не забывайте в каком модуле вы находитесь, решайте задание с флагами, а не с квадратными скобками)
Что нужно сделать:

Нужно исправить код, чтобы он смог заменить O на X, o на x.
Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Строка, с совершёнными заменами.

Sample Input 1:

LOST CXNTURY - CYBERSITY | scarlord - FALSE HOPE

Sample Output 1:

LXST CXNTURY - CYBERSITY | scarlxrd - FALSE HXPE

Sample Input 2:

SHADOWBORN shadowborn

Sample Output 2:

SHADXWBXRN shadxwbxrn

'''

import re

def get_x(m):
    return {'o': 'x', 'O':'X'}[m[0]]

print(re.subn('(?i)O', get_x, input())[0])
