'''

Кодировку файла можно указать при помощи параметра encoding. По умолчанию она выставлена как UTF-8.

f = open('in.txt', encoding='utf-8')
f.close()

Задача на программирование

Прочитайте файл ex.txt , записанный в кодировке UTF-16 и запишите содержащуюся в нем информацию в переменную answer. Затем дополните файл ex.txt новой строкой hacked.

Тестовый пример файла:

# исходные данные в ex.txt
my first line

# результат в ex.txt
my first line
hacked

Как протестировать ваше решение? 

    Создайте в отдельной папке файл ex.txt.
    Наполните его текстом в кодировке UTF-16. Это можно сделать к примеру следующей программой: f = open('ex.txt', 'w', encoding='utf-16');f.write('my text')
    Создайте в той же папке файл main.py.
    Напишите программу, решающую поставленную задачу.
    Проверьте, что все работает, запустив программу.
    Попробуйте изменить входной текст на какой-то другой.
    Отправьте ваше итоговое решение в тестирующую систему.
    В случае, если решение неправильное, посмотрите подсказку к решению. Если она не помогла – напишите комментарий 🦍.

'''

with open('ex.txt', 'r', encoding='utf-16') as f:
    answer = f.read()

with open('ex.txt', 'a', encoding='utf-16') as f:
    f.write('\nhacked')
