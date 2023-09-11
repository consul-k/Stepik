'''

Вам доступен текстовый файл file.txt, набранный латиницей. 
Напишите программу, которая выводит количество букв латинского алфавита, слов и строк. Выведите три найденных числа в формате, приведенном в примере.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести три найденных числа в формате, приведенном в примере.

Примечание 1. Если бы файл file.txt содержал строки:

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

то результатом было бы:

Input file contains:
108 letters 
20 words 
4 lines 

Примечание 2. Словом называется последовательность из непробельных символов. Например, строка

abc a21 67pop    qwert bo7ok 83456

содержит 66 слов: abc, a21, 67pop, qwert, bo7ok, 83456.

'''

with open('file.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    count_lines = len(lines)
    count_words = 0
    all_letters = []
    for line in lines:
        l = [i for i in line.split()]
        count_words += len(l)
        for letter in line.strip():
            if letter not in (' ?"/:,-.!') and not letter.isdigit():
                all_letters.append(letter)
    print(f'Input file contains:\n{len(all_letters)} letters\n{count_words} words\n{count_lines} lines')
