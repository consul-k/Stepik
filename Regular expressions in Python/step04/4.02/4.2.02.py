'''

Получите список кортежей с логином, паролем, и токеном.
Что нужно сделать:

Нужно найти логин, пароль, и токен:

    Логин состоит из 0-9
    Пароль состоит из a-z, A-Z, 0-9
    Токен состоит из a-z, 0-9
    Длина минимум 1 символ

Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Список кортежей с логином, паролем, токеном, если они найдены в тексте. Если их нет - пустой список.

Sample Input 1:

15073073928:j7jzvKkcrojW4W2G:bde5ef73cb767c9d949717978467e5a798ce70c1a67fdbeeb2744caf6a2c87d034a8d74beeab95cbb88a5 13345187013:SLkeIUOZqJ7Ddu5:177eafc83a25a3924c6f9593c7619ac3199d585a613d1341c87c32790014a975642865bbacfb9e5933da8 15715705448:hqQ5lJxuVX2sTuJj:cb3694f38d146847f758c36e79200f160a141a76d57af62ffe3d25659f8434976a2097712318cd1eed6c7 12368040749:Iw2DeXGe4xnqJLxN:8277679e1a629144e7b9a02046ed829d1a89d3662abb23ad84d710a5a545f98ba79b585ed5733b98455d4

Sample Output 1:

[('15073073928', 'j7jzvKkcrojW4W2G', 'bde5ef73cb767c9d949717978467e5a798ce70c1a67fdbeeb2744caf6a2c87d034a8d74beeab95cbb88a5'), ('13345187013', 'SLkeIUOZqJ7Ddu5', '177eafc83a25a3924c6f9593c7619ac3199d585a613d1341c87c32790014a975642865bbacfb9e5933da8'), ('15715705448', 'hqQ5lJxuVX2sTuJj', 'cb3694f38d146847f758c36e79200f160a141a76d57af62ffe3d25659f8434976a2097712318cd1eed6c7'), ('12368040749', 'Iw2DeXGe4xnqJLxN', '8277679e1a629144e7b9a02046ed829d1a89d3662abb23ad84d710a5a545f98ba79b585ed5733b98455d4')]

Sample Input 2:

75043073928:сщАИЦ93:вФЩЗАОфывфФЫСмыва ofidausdoda:djas9h0DAasd:177eafc83a25a3924c6f9593cdasaa85a613d1341c87c32790014a975642865bbacfb9e5933da8

Sample Output 2:

[]

'''

import re

result = re.findall(r'([0-9]+):([a-zA-Z0-9]+):([a-z0-9]+)', input())
print(result)
