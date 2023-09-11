'''

Обратный порядок

Вам доступен текстовый файл data.txt, в котором записаны строки текста. 
Напишите программу, выводящую все строки данного файла в обратном порядке: сначала последнюю, затем предпоследнюю и т.д.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести строки указанного файла в обратном порядке.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Используйте менеджер контекста 🙂.

Примечание 3. Получить список всех строк файла можно при помощи метода readlines().

Примечание 4. Не забывайте про символ конца строки '\n'.

'''

with open('data.txt', 'r', encoding='utf-8') as file:
    s = [line.strip() for line in file.readlines()]
    for i in s[::-1]:
        print(i)
