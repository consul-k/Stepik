'''

На вход программе подается строка с именем текстового файла. Напишите программу, которая выводит на экран его содержимое.

Формат входных данных
На вход программе подается строка текста с именем существующего текстового файла.

Формат выходных данных
Программа должна вывести содержимое указанного файла.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Не забудьте закрыть файл 🙂.

'''

file = open(input())
print(file.read())
file.close()
