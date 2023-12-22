'''

Главный бухгалтер компании "Рога и копыта" случайно удалил ведомость с начисленной зарплатой. 
К счастью, у него сохранились расчётные листки всех сотрудников. Помогите по этим расчётным листкам восстановить зарплатную ведомость. 
Архив с расчётными листками доступен по ссылке https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip 
(вы можете скачать и распаковать его вручную или самостоятельно научиться делать это с помощью скрипта на Питоне).

Ведомость должна содержать 1000 строк, в каждой строке должно быть указано ФИО сотрудника и, через пробел, его зарплата. 
Сотрудники должны быть упорядочены по алфавиту.

'''

import urllib.request
import zipfile
import openpyxl

urllib.request.urlretrieve('https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip', 'rogaikopyta.zip')

with zipfile.ZipFile('rogaikopyta.zip', 'r') as zip_ref:
    zip_ref.extractall('.')

#список всех сотрудников с зарплатой
l_data = []

for i in range(1,1001):
    book = openpyxl.open(f'{i}.xlsx', read_only=True)
    sheet = book.worksheets[0]

    #отдельный сотрудник
    worker = (sheet[2][1].value, sheet[2][3].value)
    l_data.append(worker)

#файл со списком сотрудников и зарплатой
res = open('result.txt', 'a+')
for i in sorted(l_data, key= lambda x: x[0]):
    line = ' '.join(str(x) for x in i)
    res.write(line + '\n')
res.close()
