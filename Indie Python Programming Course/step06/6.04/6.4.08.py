'''

Напишите программу, которая печатает словарь alphabet, где ключи  - строчные английские символы, а значения - порядковые номера букв в алфавите начиная с 1.

Начало вашего словаря должны быть таким {"a": 1, "b": 2 ... }

В качестве ответа распечатайте полученный словарь alphabet

Весь английский алфавит можно взять в переменной ascii_lowercase из модуля string:

from string import ascii_lowercase
print(ascii_lowercase)

Sample Input:

Sample Output:

{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

'''

from string import ascii_lowercase

alphabet = {}
cnt = 1
for i in ascii_lowercase:
    alphabet[i] = cnt
    cnt += 1
print(alphabet)
